# -*- coding: utf-8 -*-
def sayHello(name = "dostum."):
    print("Merhaba " + name)

sayHello("Erman.")
sayHello()

def sayHello2(name = "Dostum", surname = "Naber"):
    print("Merhaba " + name + " " + surname)
    
sayHello2()
sayHello2("Erman")

#%%
def triangelCalculateArea(a,b):
    return a*b/2

area = triangelCalculateArea(2, 3)
print(area)

#%%
triangelCalculateArea2 = lambda a,b : a*b/2

print(triangelCalculateArea2(3,6))

print(type(triangelCalculateArea2))

x = triangelCalculateArea2

print(x(4,5))