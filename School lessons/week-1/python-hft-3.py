print("X Giyim mağazasına hoşgeldiniz ");

trousers_piece = int(input(" pantolon adetini giriniz = "));
shirt_piece = int(input(" Tişört adetini giriniz = "));
skirt_piece = int(input("Etek adetini giriniz = "));
socks_piece =int(input("Çorap adetini giriniz = "));
jacket_piece= int(input("Ceket adetini giriniz = "))


trousers_price = int(input("pantolon fiyatını giriniz = "));
shirt_price = int(input("Tişört  fiyatını girin1iz = "));
skirt_price = int(input("Etek fiyatını giriniz = "));
socks_price = int(input("Çorap fiyatını giriniz =  "));
jacket_price = int(input("Ceket fiyatını giriniz = "));


trousers_total = trousers_piece* trousers_price;
shirt_total = shirt_piece*shirt_price;
skirt_total = skirt_piece*skirt_price;
socks_total = socks_piece * socks_price;
jacket_totAL = jacket_piece*jacket_price;

total = 0 ;
total = trousers_total + shirt_total + skirt_total + socks_total+jacket_totAL ;

if total>=0 and total<=100:
    total= total - total * .5;
    print("Yüzde 5 indirim kazandınız ,ödeyeceğiniz tutar = " , total); 
elif total>100 and total<=2000:
    total=total-total* .15;
    print("Yüzde 15 indirim kazandınız ,ödeyeceğiniz tutar = " , total);
elif total>2000 and total<=5000:
    total=total-total* .25;
    print("Yüzde 25 indirim kazandınız ,ödeyeceğiniz tutar = " , total);
else:
    total=total-total* .50
    print(" Yüzde 50 indirim kazandınız ,  ödeyeceğiniz tutar  = ", total);
     