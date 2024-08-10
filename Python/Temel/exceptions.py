# -*- coding: utf-8 -*-
try:
    sayi = int(input("Bir sayi giriniz: "))
except ValueError:
    print("Tip uyusmazligi: Lutfen sayi giriniz.")
except ZeroDivisionError:
    print("Payda sifir olamaz.")
except:
    print("Bir hata meydena geldi!")
