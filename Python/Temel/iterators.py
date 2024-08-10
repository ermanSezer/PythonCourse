# -*- coding: utf-8 -*-

sehirler =["Ankara", "Izmir", "Istanbul"]

iterator = iter(sehirler)

print(next(iterator))
print(next(iterator))
print(next(iterator))

for sehir in sehirler:
    print(sehir)
