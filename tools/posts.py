from brand import *
W,H=1080,1350
def cover(path,n,tot,title,sub):
    im,d=frame(RED,CREAM,n,tot); d.rectangle([80,330,200,342],fill=CREAM)
    y=text(d,(80,380),title,f('InterDisplay-Bold.otf',100),CREAM,920,1.12)
    text(d,(80,y+40),sub,f('Inter-Medium.otf',46),PINK,900)
    d.text((80,H-200),'Saqlab qo‘ying va o‘ngga suring  →',font=f('Inter-SemiBold.otf',34),fill=CREAM)
    im.save(path)
def cta(path,n,tot):
    im,d=frame(INK,CREAM,n,tot)
    d.text((80,300),'MASHQ UCHUN',font=f('Inter-Bold.otf',34),fill=(240,90,110))
    y=text(d,(80,360),'Turk tili Multilevel 2027',f('InterDisplay-Bold.otf',88),CREAM,920,1.1)
    y=text(d,(80,y+10),'Okuma mock testlar to‘plami',f('InterDisplay-Medium.otf',58),SOFT,920,1.15)+50
    for b in ['30 ta to‘liq test','B1 · B2 · C1 darajalari','Javoblar va qisqa izohlar']:
        d.ellipse([80,y+16,98,y+34],fill=RED); d.text((125,y),b,font=f('Inter-Medium.otf',42),fill=CREAM); y+=72
    d.rounded_rectangle([80,H-330,W-80,H-200],radius=24,fill=RED)
    d.text((120,H-300),'Batafsil: Telegram @Akhmad_Axtamovich',font=f('Inter-Bold.otf',40),fill=CREAM)
    im.save(path)
# --- Post A: bog'lovchilar
def words(path,n,tot,items):
    im,d=frame(CREAM,RED,n,tot); y=210
    for tr,uz,ex in items:
        d.text((80,y),tr,font=f('InterDisplay-Bold.otf',64),fill=RED)
        d.text((80,y+82),'— '+uz,font=f('Inter-SemiBold.otf',38),fill=INK)
        y=text(d,(80,y+138),ex,f('Inter-Regular.otf',32),MUTE,920,1.35)+42
    im.save(path)
cover('w1/A1.png',1,4,'Okumada fikrni burib yuboradigan 8 ta so‘z','Bu bog‘lovchilarni bilsangiz, matnni tezroq va to‘g‘ri tushunasiz')
words('w1/A2.png',2,4,[('ama / fakat','lekin, biroq','Ucuz, ama kaliteli değil.'),('oysa','holbuki','Kolay sandım, oysa çok zordu.'),('çünkü','chunki','Gelemedim, çünkü hastaydım.'),('bu nedenle','shu sababli','Yağmur yağdı, bu nedenle maç ertelendi.')])
words('w1/A3.png',3,4,[('ayrıca','bundan tashqari','Ayrıca her test için cevap anahtarı var.'),('örneğin','masalan','Bazı kelimeler zordur, örneğin “gerçi”.'),('gerçi','to‘g‘ri, garchi','Gerçi yorgundum, yine de çalıştım.'),('sonuç olarak','natijada','Sonuç olarak sınavı geçti.')])
cta('w1/A4.png',4,4)
# --- Post B: 5 topshiriq turi
def tasks(path,n,tot,items):
    im,d=frame(CREAM,RED,n,tot); y=220
    for num,title,body,tip in items:
        d.text((80,y),num,font=f('InterDisplay-Bold.otf',110),fill=RED)
        y2=text(d,(240,y+14),title,f('InterDisplay-Bold.otf',50),INK,760,1.12)
        y2=text(d,(240,y2+8),body,f('Inter-Regular.otf',34),MUTE,760,1.35)
        y=text(d,(240,y2+6),'Maslahat: '+tip,f('Inter-SemiBold.otf',32),RED,760,1.35)+56
    im.save(path)
cover('w1/B1.png',1,4,'Okuma bo‘limida 5 xil topshiriq bor','Har birini qanday yechish kerak? Qisqa va aniq')
tasks('w1/B2.png',2,4,[('1','Boşluk doldurma','Matndagi bo‘shliqqa mos so‘z yoki jumlani qo‘yasiz.','bo‘shliqdan oldingi va keyingi jumlani o‘qing.'),
 ('2','Durum – metin eşleştirme','Vaziyatlarni ularga mos matn bilan moslashtirasiz.','har bir vaziyatdagi asosiy shartni belgilab oling.'),
 ('3','Paragraf – başlık eşleştirme','Har bir paragrafga mos sarlavha tanlaysiz.','paragrafning birinchi va oxirgi jumlasiga qarang.')])
tasks('w1/B3.png',3,4,[('4','Uzun metin','Uzun matn va unga oid savollar.','savollar ko‘pincha matn tartibida keladi.'),
 ('5','A–E paragraflı metin','Fikr yoki ma’lumot qaysi paragrafda ekanini topasiz.','kalit so‘zlarni emas, ma’nosini qidiring.')])
cta('w1/B4.png',4,4)
