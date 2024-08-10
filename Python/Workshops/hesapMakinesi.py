# -*- coding: utf-8 -*-
#%% Benim yazdigim kodlar
def topla(sayi1, sayi2):
    print("Girdiginiz sayilarin toplami: " + str(sayi1 + sayi2))
def cikar(sayi1, sayi2):
    print("Girdiginiz sayilarin toplami: " + str(sayi1 - sayi2))
def carp(sayi1, sayi2):
    print("Girdiginiz sayilarin toplami: " + str(sayi1 * sayi2))
def bol(sayi1, sayi2):
    print("Girdiginiz sayilarin toplami: " + str(sayi1 / sayi2))
    
print("""
      Operasyon needir?
      1 : Topla
      2 : Cikar
      3 : Carp
      4 : Bol
      """)

x = int(input(""))

sayi1 = int(input("Islem yapmak istediginiz 1. sayiyi giriniz: "))
sayi2 = int(input("Islem yapmak istediginiz 2. sayiyi giriniz: "))
    
if x ==1:
    topla(sayi1, sayi2)
elif x==2:
    cikar(sayi1, sayi2)
elif x == 3:
    carp(sayi1, sayi2)
elif x ==4:
    bol(sayi1, sayi2)
else:
    print("0 ya da hatali sayi girdiniz.")
    
#%% Engin Hocanin yazdigi kodlar
def add(number1, number2):
    return number1 + number2
def subtraction(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    return number1 / number2
print("Operasyon:")
print("1 : Topla")
print("2 : Cikar")
print("3 : Carp")
print("4 : Bol")

secenek = input("Operasyon seciminiz?")

number1 = int(input("Birinci sayi?"))
number2 = int(input("Ikinci sayi?"))

if secenek == '1':
    print("Toplam: " + str(add(number1, number2)))
elif secenek == '2':
    print("Cikarma: " + str(subtraction(number1, number2)))
elif secenek == '3':
    print("Carpma:" + str(multiply(number1, number2)) )
elif secenek == '4':
    print("Bolme: " + str(divide(number1, number2)))
else:
    print("Gecersiz secenek")
    
    
    
    
    
    
    
    
    
    
    



    
    
    
    
    
    
    
    
    
    