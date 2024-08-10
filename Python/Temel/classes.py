# -*- coding: utf-8 -*-
#%%
class Matematik:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
    
matematik = Matematik(2, 70)

#%% Property
class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Erman", "Sezer", 34)

print(person1.firstName)

class Worker(Person):
    def __init__(self, salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
ahmet = Worker()

ahmet.















