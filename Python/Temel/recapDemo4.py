# -*- coding: utf-8 -*-

students = ["Erman", "Sezer", "Serhat", "Batuhan", "Mehmet"]

fileToAppend = open("students", "a")

for student in students:
    fileToAppend.write(student)
    fileToAppend.write("\n")
    
fileToAppend.close()
