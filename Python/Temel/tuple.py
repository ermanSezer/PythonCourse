# -*- coding: utf-8 -*-
tupleList = (2, 4, 6, "Kirklareli", (1,3,5), [7,8])
list = [2, 4, 6, "Kirklareli", [9,3,8], (1,8)]

list[0] = 3
#tupleList[0] = 3
tupleValue = ("Erman",)
print(type(tupleValue))

print(tupleList[1:2])
print(list[1:2])

print(tupleList[-2])
print(list[-2])

print(type(tupleList))
print(type(list))
print(tupleList)
print(list)
print(len(tupleList))
print(len(list))