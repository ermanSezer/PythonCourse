# -*- coding: utf-8 -*-
#substring
message = "Merhaba dunya"

print(message[2:5])

newMessage = message[:5]

print(newMessage)

#len functions

print(message[len(message)-1:len(message)])

#Lower upper

print(message.upper())
print(message.lower())  

#Replace
print(message.replace("u","ü"))

print(message.replace("a", "4"))

# Split and Strip
information = "Erman;SEZER;34;Kirklareli".strip()
print(information.split()) #Creates a array
print("Adi: " + information.split(";")[0])

#input
name = input("Adiniz lutfen: ")
number = input("Bir sayi giriniz:")
number2 = input("Ikinci sayiyi giriniz: ")
print(int(number) + int(number2))
