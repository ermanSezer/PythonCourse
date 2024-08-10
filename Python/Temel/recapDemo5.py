# -*- coding: utf-8 -*-
import sys
liste = [7, 'erman', 0, 3, "6"]

for i in liste:
    try:
        print("Sayi: " + str(i))
        sonuc = 1/int(i)
        print("Sonuc: " + str(sonuc))
    except ValueError:
        print(str(i) + " bir sayi degil.")
    except ZeroDivisionError:
        print(str(i) + " sifira bolme hatasi")
    except:
        print(str(i) + " hesaplanamadi.")
        print("Sistem diyor ki : " + str(sys.exc_info()[0]))
    finally:
        print("islemler bitti.")