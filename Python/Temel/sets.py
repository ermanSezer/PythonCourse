# -*- coding: utf-8 -*-
studentsSet = {"Erman", "Sezer", "Serhat", "Naci"}
studentsSet2 = set("Ali", "Veli", "Mehmet", "Ahmet")
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Sezer" in studentsSet)

if "Sezer" in studentsSet:
    print("Listede var.")
    
studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["Merve", "Mert", "Selin"])
print(studentsSet)

print(len(studentsSet))
studentsSet.remove("Selin")
print(len(studentsSet))

studentsSet.discard("Selin")
print(len(studentsSet))

studentsSet.clear()
print(len(studentsSet))
print(studentsSet)

del studentsSet
print(studentsSet)












