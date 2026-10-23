from PIL import Image, ImageDraw, ImageFont
F='/usr/share/fonts/opentype/inter/'
def f(n,s): return ImageFont.truetype(F+n,s)
RED=(200,16,46); CREAM=(250,245,236); INK=(28,24,26); MUTE=(110,100,100); PINK=(255,220,224); SOFT=(240,200,205)
def wrap(d,t,fn,w):
    out=[]
    for para in t.split('\n'):
        line=''
        for word in para.split(' '):
            tt=(line+' '+word).strip()
            if d.textlength(tt,font=fn)<=w: line=tt
            else: out.append(line); line=word
        out.append(line)
    return out
def text(d,xy,t,fn,fill,w,gap=1.25,center=False,W=1080):
    x,y=xy
    for l in wrap(d,t,fn,w):
        xx=(W-d.textlength(l,font=fn))/2 if center else x
        d.text((xx,y),l,font=fn,fill=fill); y+=int(fn.size*gap)
    return y
def frame(bg,fg,n,tot,W=1080,H=1350):
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
    d.text((80,70),'TURKISH CENTER',font=f('Inter-Bold.otf',30),fill=fg)
    if n:
        s=f'{n}/{tot}'; d.text((W-80-d.textlength(s,font=f('Inter-Medium.otf',30)),70),s,font=f('Inter-Medium.otf',30),fill=fg)
    d.text((80,H-110),'@turkish_centerr',font=f('Inter-Medium.otf',30),fill=fg)
    return im,d
