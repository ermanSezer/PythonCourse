# -*- coding: utf-8 -*-
citys = ["Ankara", "Istanbul", "Izmir"]
#%% For intro
for city in citys:
    if city == "Ankara":
        continue
    print(city + " icin kod: " + city[0:3])
    print("*******")
    

#%% For range
for x in range(1,10,2):
    print(x)