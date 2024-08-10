# -*- coding: utf-8 -*-
#%% Benim yazdigim kodlar
number = int(input("Faktoriyel hesabi icin bir sayi giriniz:"))
faktoriyel = 1
counter = 1

if number<0:
    print("Sifirdan buyuk bir sayi giriniz.")
elif number ==0:
    print("Sifirin faktoriyeli 1 dir.")
elif number>0: 
    while counter <= number:
        faktoriyel = faktoriyel * counter
        counter = counter + 1
    print("Girdiginiz sayinin faktoriyeli: " , faktoriyel)
    
#%% Engin Hocanin yazdigi kodlar
sayi = int(input("Sayi: "))
faktoriyel2 = 1
if sayi < 0:
    print("Negatif sayilarin faktoriyeli hesaplanamaz.")
elif sayi==0:
    print("Sonuc : 1")
else:
    for i in range(1, sayi+1):
        faktoriyel2 = faktoriyel2 * i
    print("Sonuc: ", faktoriyel2)