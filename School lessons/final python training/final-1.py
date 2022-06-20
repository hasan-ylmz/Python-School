# Örnek sınav sorusu 
# Bir firmada bir kişinin maaşını hesaplamak için aşağıda belirtilen kriterler kullanılmaktadır .
# 1- Kişinin adını ve soyadını alınız .
# 2- Kişinin görevini alınız , Müdür(M) , sekreter(S), işçi(İ)
# 3- Müdür ham maaşı 15.000 işçi=9000 , sekreter=8000,
# 4- Çalışan çocuk sayısını alın, her bir çocuk için 50 tl yardım yapınız
# 5- Mesai saatini alın, o ayda ekstra çalıştığı mesai saati , 1 saatlik= 50 tl . 
# 6- Hediye promosyon , her bir çalışan çalıştığı ayda 100-300 arasında rastgle ikramiye alır. 
# 7- Eğer mesai saati aylık 30 saatin üzerinde ise maaşının ise 
#    maaşının %5i kadar ekstra prim ikramiyesi alır 
# 8- Bu verilerle brüt maaşı hesaplayacağız .
# 9- brüt maaşı üzerinden %0.5 damga vergisi kesilecek , 
#    20.000-25.000 arası ise %20 gelir vergisi kes ,25.000 üzeri ise %25 gelir vergisi kesilecek .
# 10- Net maaşı hesapla .

# Maaş detaylarını ekrana yazdır .


import random

name= str(input("isminizi giriniz = "))
lastName  = str(input("Soyadınızı giriniz = "))
Job = str(input("Yaptığınız işi giriniz : Müdür(M) , Sekreter(S), İşçi(I)"))
Children = int(input("Kaç çocuğunuz var ? "))
shift= int(input("Bu ay kaç saat mesai yaptınız ? "))

ıkramıye = random.randrange(100,300);

M_hmmaas =  15.000;
S_hmmaas = 8000;
I_hmmaas=  9000;


topchildren =Children *int(50)
topshift = shift* int(50);

topmaas =  0;
if shift>30:
    topmaas = (topshift * (5/100)) +topshift +topchildren + ıkramıye;


print("Sayın " ,name ,lastName, " " ," Bu ay " ,shift, " saat mesai yaptınız ." )
print(" Mesai ücretiniz ",topshift , " Çocuk yardımı  ", topchildren   )  