# Örnek sınav sorusu 
# Bir firmada bir kişinin maaşını hesaplamak için aşağıda belirtilen kriterler kullanılmaktadır .
# 1- Kişinin adını ve soyadını alınız .
# 2- Kişinin görevini alınız , Müdür(M) , sekreter(S), işçi(İ)
# 3- Müdür ham maaşı 15.000 işçi=9000 , sekreter=8000,
# 4- Çalışan çocuk sayısını alın, her bir çocuk için 50 tl yardım yapınız
# 5- Mesai saatini alın, o ayda ekstra çalıştığı mesai saati , 1 saatlik= 10 tl . 
# 6- Hediye promosyon , her bir çalışan çalıştığı ayda 100-300 arasında rastgle ikramiye alır. 
# 7- Eğer mesai saati aylık 30 saatin üzerinde ise maaşının ise 
#    maaşının %5i kadar ekstra prim ikramiyesi alır 
# 8- Bu verilerle brüt maaşı hesaplayacağız .
# 9- brüt maaşı üzerinden %0.5 damga vergisi kesilecek , 
#    10.000-20.000 arası ise %15 gelir vergisi kes,20.000-25.000 arası ise %20 gelir vergisi kes ,25.000 üzeri ise %25 gelir vergisi kesilecek .
# 10- Net maaşı hesapla .


# Maaş detaylarını ekrana yazdır .

import random
## İkramiye
ikramiye = random.randrange(100,300);

name= str(input("isminizi giriniz = "))
lastName  = str(input("Soyadınızı giriniz = "))
Job = str(input("Yaptığınız işi giriniz : Müdür(M) , Sekreter(S), İşçi(I)"))
Children = int(input("Kaç çocuğunuz var ? "))
mesai = int(input("Bu ay kaç saat  mesai yaptınız ? "))

Topmaas = 0;
Brutmaas = 0;
hammaas = 0;
cocukmaas= 0;
mesaikazanc = 0;
gyazi = "";

if Job =="M":
    hammaas=15.000;
    gyazi="Müdür";
elif Job== "S":
    hammaas=8.000;
    gyazi="Sekreter";
elif Job== "I":
    hammas = 9.000;
    gyazi =" İşçi";

Brutmaas = hammaas+(Children*50)+ikramiye;

if mesai>30:
    Brutmaas=Brutmaas+(mesai*10)+(hammaas*0.05)
    mesaikazanc = (mesai*10)+(hammaas*0.05)
else:
    Brutmaas=Brutmaas+(mesai*60)
    mesaikazanc = (mesai*10)

damgavergisi = Brutmaas- (Brutmaas* 0.005)
gelirvergioran = 0;

if Brutmaas>=10000 and Brutmaas<20000:   
    Brutmaas=Brutmaas-(Brutmaas * .15);
    gelirvergioran=15;
elif Brutmaas>=20000 and Brutmaas<25000:
    Brutmaas= Brutmaas(Brutmaas* .20);
    gelirvergioran=20;
elif Brutmaas>25000:
    Brutmaas = Brutmaas- (Brutmaas* .25)
    gelirvergioran =25;

cocukpara = Children*50;

print("Sayın ",name, " ", lastName);
print("Göreviniz : ", Job);
print("Çocuk sayısı" , Children);
print("Çocuk yardımı = ", cocukmaas);
print("Bu ay yaptığınız mesai :", mesai);
print("Aylık promosyonunuz :" ,ikramiye);
print("Hammaaşınız = ", )




