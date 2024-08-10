# -*- coding: utf-8 -*-
#%% Benim yazdigim kodlar
A = [                        #Sutun:0    Sutun:1     Sutun:2
     [1, 2, 3],   #satir:0   d[0,0]      d[0,1]       d[0,2]
     [4, 5, 6],   #satir:1   d[1,0]      d[1,1]       d[1,2]
     [7, 8, 9],   #satir:2   d[2,0]      d[2,1]       d[2,2]
     ]

B = [
     [0, 2, 3],
     [4, 3, 5],
     [7, 1, 2],
     ]

C = [
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     ]

# satirlarda gez
for i in range(len(A)):
    # sutunlarda gez
    for j in range(len(B)):
        C[i][j] = A[i][j] + B[i][j]

for r in C:
    print(r)

#%% Engin Hocanin yazdigi

x = [[1, 3, 5], [2, 4, 1], [1, 5, 7]]
y = [[3, 3, 4], [2, 4, 1], [3, 5, 4]]
sonuc = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j] = x[i][j] + y[i][j]
print(sonuc)













