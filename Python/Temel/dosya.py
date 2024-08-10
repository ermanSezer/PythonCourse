# -*- coding: utf-8 -*-
# r read, w write, a append, x create

f = open("musteriler.txt")

#print(f.read())
#print(f.readline())
for l in f:
    print(l)
    
f.close()
#%%
filetoAppend = open("ogrenciler.txt", "a")
filetoAppend.write("\n")
filetoAppend.write("Sezer")
filetoAppend.close()

#%%
import os
if os.path.exists("ogrenciler.txt"):
    print("Dosya var!")
#os.remove("ogrenciler.txt")
os.rmdir("empty")