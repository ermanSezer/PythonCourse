# -*- coding: utf-8 -*-
dictionary = {
            "book" : "kitap",
            "table" : "masa",
             "eraser" : "silgi"   
    }

myDictionary = dict(kitap = "book", masa = "table", silgi = "eraser")
dictionary["table"] = "yemek masasi"
dictionary["pencil"] = "kalem"
del(dictionary["book"])
print(len(dictionary))