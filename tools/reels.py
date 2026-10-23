import subprocess, sys
from brand import *
W,H=1080,1920; FPS=30
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
def base(bg=RED,fg=CREAM):
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
    d.text((80,140),'TURKISH CENTER',font=f('Inter-Bold.otf',36),fill=fg)
    d.text((80,H-220),'@turkish_centerr',font=f('Inter-Medium.otf',36),fill=fg)
    return im,d
def layer(im,draw_fn,t):
    # fade+slide in: draw on transparent then composite
    a=ease(t)
    if a<=0: return
    L=Image.new('RGBA',(W,H),(0,0,0,0)); dl=ImageDraw.Draw(L); draw_fn(dl)
    if a<1:
        al=L.split()[3].point(lambda p:int(p*a)); L.putalpha(al)
        L=L.transform(L.size,Image.AFFINE,(1,0,0,0,1,-int((1-a)*40)))
    im.paste(L,(0,0),L)
def render(scenes,out,dur):
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
        '-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p',
        '-c:a','aac','-b:a','128k','-movflags','+faststart',out],stdin=subprocess.PIPE)
    for i in range(int(dur*FPS)):
        t=i/FPS; im=scenes(t); p.stdin.write(im.tobytes())
    p.stdin.close(); p.wait()
# ---------- Reel 1: quiz
def quiz(t):
    if t<2.2:
        im,d=base()
        layer(im,lambda d:text(d,(80,700),'1 daqiqalik test',f('Inter-SemiBold.otf',54),PINK,920),t/0.5)
        layer(im,lambda d:text(d,(80,790),'Bo‘shliqqa qaysi so‘z mos keladi?',f('InterDisplay-Bold.otf',104),CREAM,920,1.1),(t-0.3)/0.6)
        return im
    im,d=base(CREAM,RED); s=t-2.2
    q='Hava çok soğuktu, ______ dışarı çıkmadık.'
    layer(im,lambda d:text(d,(80,420),q,f('InterDisplay-Bold.otf',78),INK,920,1.2),s/0.5)
    opts=[('A','ama'),('B','bu yüzden'),('C','oysa')]
    reveal=s>=7.0
    for k,(L,w) in enumerate(opts):
        y=820+k*170
        def dr(d,L=L,w=w,y=y):
            good=reveal and L=='B'; bad=reveal and L!='B'
            fill=(34,139,76) if good else ((235,228,220) if bad else (255,255,255))
            d.rounded_rectangle([80,y,W-80,y+130],radius=28,fill=fill,outline=(225,215,205),width=3)
            col=CREAM if good else (MUTE if bad else INK)
            d.text((130,y+34),f'{L})  {w}',font=f('Inter-SemiBold.otf',56),fill=col)
        layer(im,dr,(s-0.6-k*0.25)/0.4)
    if 2.0<=s<7.0:
        n=3-int((s-2.0)//1.6) if s<6.8 else 1
        n=max(1,min(3,3-int((s-2.0)/1.66)))
        def cd(d,n=n): 
            d.ellipse([W/2-90,1380,W/2+90,1560],fill=RED); tx=str(n); fn=f('InterDisplay-Bold.otf',110)
            d.text((W/2-d.textlength(tx,font=fn)/2,1395),tx,font=fn,fill=CREAM)
        layer(im,cd,1)
        d.text((80,1620),'Javobingizni izohda yozing',font=f('Inter-Medium.otf',40),fill=MUTE)
    if reveal:
        layer(im,lambda d:text(d,(80,1360),'To‘g‘ri javob: B — bu yüzden (shuning uchun). Sovuq sabab, uyda qolish natija.',f('Inter-SemiBold.otf',44),INK,920,1.3),(s-7.3)/0.5)
    if s>=11.5:
        im,d=base(INK,CREAM); u=s-11.5
        layer(im,lambda d:text(d,(80,720),'Shunday testlar 30 ta to‘plamda',f('InterDisplay-Bold.otf',90),CREAM,920,1.12),u/0.5)
        layer(im,lambda d:text(d,(80,1060),'Turk tili Multilevel 2027 — Okuma mock testlar to‘plami',f('Inter-Medium.otf',48),SOFT,920,1.3),(u-0.3)/0.5)
        def b(d):
            d.rounded_rectangle([80,1300,W-80,1440],radius=28,fill=RED)
            t2='Telegram: @Akhmad_Axtamovich'; fn=f('Inter-Bold.otf',48); d.text((W/2-d.textlength(t2,font=fn)/2,1342),t2,font=fn,fill=CREAM)
        layer(im,b,(u-0.6)/0.5)
    return im
# ---------- Reel 2: Kolay gelsin
def phrase(t):
    if t<3.0:
        im,d=base()
        layer(im,lambda d:text(d,(80,620),'Turklar kuniga 100 marta aytadigan ibora',f('Inter-SemiBold.otf',54),PINK,920,1.3),t/0.5)
        layer(im,lambda d:text(d,(80,820),'“Kolay gelsin”',f('InterDisplay-Bold.otf',140),CREAM,920,1.1),(t-0.5)/0.6)
        return im
    if t<8.5:
        s=t-3.0; im,d=base(CREAM,RED)
        layer(im,lambda d:d.text((80,420),'Ma’nosi',font=f('Inter-Bold.otf',40),fill=RED),s/0.4)
        layer(im,lambda d:text(d,(80,490),'“Ishingiz oson bo‘lsin”, “Qiyin bo‘lmasin”',f('InterDisplay-Bold.otf',80),INK,920,1.15),(s-0.2)/0.5)
        layer(im,lambda d:d.text((80,900),'Qachon aytiladi?',font=f('Inter-Bold.otf',40),fill=RED),(s-1.2)/0.4)
        for k,l in enumerate(['Ishlayotgan odamga salom berganda','Do‘kondan chiqib ketayotganda','Hamkasbingiz bilan xayrlashganda']):
            def dr(d,l=l,y=980+k*110):
                d.ellipse([80,y+18,100,y+38],fill=RED); d.text((130,y),l,font=f('Inter-Medium.otf',46),fill=INK)
            layer(im,dr,(s-1.6-k*0.5)/0.4)
        return im
    if t<14.0:
        s=t-8.5; im,d=base(CREAM,RED)
        layer(im,lambda d:d.text((80,420),'Misol',font=f('Inter-Bold.otf',40),fill=RED),s/0.4)
        def bub(d,y,who,txt,right=False,col=(255,255,255),tc=INK):
            fn=f('Inter-SemiBold.otf',54); w=d.textlength(txt,font=fn)+100
            x=W-80-w if right else 80
            d.rounded_rectangle([x,y,x+w,y+130],radius=40,fill=col)
            d.text((x+50,y+34),txt,font=fn,fill=tc)
            d.text((x+10,y-50),who,font=f('Inter-Medium.otf',34),fill=MUTE)
        layer(im,lambda d:bub(d,600,'Siz:','Merhaba, kolay gelsin!'),(s-0.3)/0.5)
        layer(im,lambda d:bub(d,880,'Sotuvchi:','Sağ ol!',True,RED,CREAM),(s-1.8)/0.5)
        layer(im,lambda d:text(d,(80,1200),'Javob: “Sağ ol” yoki “Teşekkürler” deyiladi.',f('Inter-Medium.otf',46),MUTE,920,1.3),(s-3.0)/0.5)
        return im
    s=t-14.0; im,d=base(INK,CREAM)
    layer(im,lambda d:text(d,(80,740),'Saqlab qo‘ying va ertaga ishlatib ko‘ring',f('InterDisplay-Bold.otf',90),CREAM,920,1.12),s/0.5)
    layer(im,lambda d:text(d,(80,1120),'Har hafta yangi iboralar: @turkish_centerr',f('Inter-Medium.otf',46),SOFT,920,1.3),(s-0.4)/0.5)
    return im
which=sys.argv[1]
if which=='1': render(quiz,'w1/R1_test.mp4',16.5)
else: render(phrase,'w1/R2_kolay_gelsin.mp4',18)
