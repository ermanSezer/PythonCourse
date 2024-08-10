# -*- coding: utf-8 -*-
#%% Benim yapamadigim :)
sentence = input("Bir cumle giriniz: ")

serialSentence = sorted(sentence)

print(serialSentence)

#%% Engin Hocanin yaptigi
cumle ="Bugun hava cok guzel"

kelimeler = cumle.split()

kelimeler.sort()

print(kelimeler)

for kelime in kelimeler:
    print(kelime)