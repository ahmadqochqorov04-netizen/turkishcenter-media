"""Original royalty-free background music generator (no samples, pure synthesis).
Usage: python3 music.py out.wav seconds bpm key mood seed
  key: note name e.g. A, C, D ; mood: minor|major
"""
import sys, numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter
SR=44100
NOTES={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def hz(m): return 440*2**((m-69)/12)
def env(n,a=0.005,d=0.3):
    t=np.arange(n)/SR; e=np.exp(-t/d); k=int(a*SR)
    if k>0: e[:k]*=np.linspace(0,1,k)
    return e
def lp(x,fc,o=2): b,a=butter(o,fc/(SR/2)); return lfilter(b,a,x)
def hp(x,fc,o=2): b,a=butter(o,fc/(SR/2),'high'); return lfilter(b,a,x)
def kick(n):
    t=np.arange(n)/SR; f=50+100*np.exp(-t*30); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*7)
def snare(n,rng):
    t=np.arange(n)/SR; return lp(hp(rng.standard_normal(n),1500),6000)*np.exp(-t*22)*0.45+np.sin(2*np.pi*190*t)*np.exp(-t*25)*0.3
def hat(n,rng):
    t=np.arange(n)/SR; return lp(hp(rng.standard_normal(n),7000,4),12000)*np.exp(-t*80)
def keys(freqs,n):
    t=np.arange(n)/SR; s=np.zeros(n)
    for f in freqs:
        for h,a in [(1,1),(2,.35),(3,.12),(4,.05)]:
            s+=a*np.sin(2*np.pi*f*h*t+0.3*np.sin(2*np.pi*5*t)*(h>1))
    return s*env(n,0.01,1.2)/len(freqs)
def pluck(f,n):
    t=np.arange(n)/SR; s=np.sign(np.sin(2*np.pi*f*t))*0.5+np.sin(2*np.pi*f*t)
    return lp(s,2500)*env(n,0.002,0.18)
def add(buf,x,i):
    j=min(len(buf),i+len(x)); 
    if i<len(buf): buf[i:j]+=x[:j-i]
def make(out,secs,bpm,key,mood,seed):
    rng=np.random.default_rng(seed)
    N=int(secs*SR); beat=60/bpm; B=int(beat*SR)
    root=48+NOTES[key]
    scale=[0,2,3,5,7,8,10] if mood=='minor' else [0,2,4,5,7,9,11]
    degs=[[0,5,2,6],[0,3,5,4],[5,3,0,4],[0,4,5,3]][seed%4] if mood=='minor' else [[0,4,5,3],[0,5,3,4],[3,4,0,5]][seed%3]
    def triad(d):
        return [root+12+scale[(d+k)%7]+12*((d+k)//7) for k in (0,2,4)]
    drums=np.zeros(N); bass=np.zeros(N); chords=np.zeros(N); lead=np.zeros(N); duck=np.ones(N)
    nbeats=int(secs/beat)+1
    penta=[0,2,4,7,9] if mood=='major' else [0,3,5,7,10]
    for b in range(nbeats):
        i=b*B; bar=b//4; d=degs[bar%4]
        if b%4==0: add(chords,keys([hz(m) for m in triad(d)],4*B),i)
        add(drums,kick(int(.4*SR)),i) if b%2==0 or (b%4==3 and rng.random()<.5) else None
        if b%2==0:
            k=int(.25*SR); e=np.ones(N); 
        if b%4 in (1,3): add(drums,snare(int(.3*SR),rng)*0.8,i)
        for h in (0,B//2): add(drums,hat(int(.08*SR),rng)*(0.25 if h else 0.15),i+h)
        bn=root-12+scale[d%7]
        for h,o in [(0,0),(B//2,12 if b%2 else 0)]:
            t=np.arange(B//2)/SR; s=np.sin(2*np.pi*hz(bn+o)*t)+0.3*np.sin(4*np.pi*hz(bn+o)*t)
            add(bass,s*env(B//2,0.005,0.25),i+h)
        if bar>=1:
            for h in (0,B//2):
                if rng.random()<0.7:
                    m=root+24+penta[rng.integers(5)]
                    add(lead,pluck(hz(m),int(.3*SR)),i+h)
        if b%2==0:
            ln=int(.25*SR); dk=1-0.45*np.exp(-np.arange(ln)/SR*12)
            j=min(N,i+ln); duck[i:j]=np.minimum(duck[i:j],dk[:j-i])
    mix=0.5*lp(drums,9000)+0.6*lp(bass,400)*duck+0.45*chords*duck+0.22*lead*duck
    # simple stereo delay/reverb
    L=mix.copy(); R=mix.copy(); dl=int(beat*0.75*SR)
    for k in range(1,4):
        g=0.25**k; L[dl*k:]+=g*mix[:-dl*k]*0.6; R[int(dl*k*1.1):]+=g*mix[:-int(dl*k*1.1)]*0.6
    st=np.stack([L,R],1)
    f=int(0.6*SR); st[:f]*=np.linspace(0,1,f)[:,None]; st[-2*f:]*=np.linspace(1,0,2*f)[:,None]
    st=st/np.max(np.abs(st))*0.85
    wavfile.write(out,SR,(st*32767).astype(np.int16))
if __name__=='__main__':
    o,s,bpm,key,mood,seed=sys.argv[1:7]; make(o,float(s),float(bpm),key,mood,int(seed))
