# -*- coding: utf-8 -*-
#Degisken ortamlara uygun programlama yapilmali -> Dinamik
students = ["Erman", "Dilek", "Akinalp", "Davut", "Guler"]
print(students[1])
students.append("Sezer")
students[2] = "Alp"
students.remove("Erman")
print(students)

#List constructor
citys = list(("Ankara", "Istanbul", "Izmir", "Ankara"))
print(citys)
print(len(citys))
#diger fonksiyonlar
# print(citys.clear())
print("Ankara sayisi: " + str(citys.count("Ankara")))
print("Ankara indexi: " + str(citys.index("Ankara")))
citys.pop(1)
citys.insert(0, "Istanbul")
citys.reverse()
print(citys)
citys3 = citys.copy()
citys2 = citys
citys2[0] = "Kirklareli"
print(citys)
print(citys3)

citys.extend(citys3)
citys.sort()
citys.reverse()
print(citys)




















