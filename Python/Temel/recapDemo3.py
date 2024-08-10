# -*- coding: utf-8 -*-
number = int(input("Sayi giriniz: "))
primeNumber = True

for x in range(2, number):
    if (number % x) == 0:
        primeNumber = False
        break

if primeNumber:
    print("Bu sayi asaldir.")
else:
    print("Bu sayi asal DEGIL!")
         
