# -*- coding: utf-8 -*-
number1 = int(input("Birinci sayiyi giriniz: "))
number2 = int(input("Ikinci sayiyi giriniz: "))
number3 = int(input("Ucuncu sayiyi giriniz: "))

if (number1 >= number2) and (number1 >= number3):
    biggestNumber = number1
elif (number2>= number1) and (number2 >= number3):
    biggestNumber = number2
else:
    biggestNumber = number3
    
print("En buyuk sayi: ", biggestNumber)
    












