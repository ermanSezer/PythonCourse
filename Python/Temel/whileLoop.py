# -*- coding: utf-8 -*-
counter = 1
sum = 0
n = int(input("1`den kaca kadar sayi toplanmasini istersiniz?"))
while counter <= n:
    sum = counter + sum
    counter = counter + 1 

print("1`den n`ye kadar olan sayilarin toplami: " , sum)