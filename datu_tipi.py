a = "5"

b = 5

c = 5.5

print(type(a))
print(type(b))
print(type(c))
print (a + a)



vards = input("Ievadi varoņa vārdu: ")
punkti = int(input("Ievadi bāzes punktus: "))
reizinatajs = float(input("Ievadi reizinātāju: "))
kopa = punkti * reizinatajs
print(vards, "ieguva", kopa, "punktus")


vards2 = input("Ievadi varoņa vārdu: ")
punkti2 = int(input("Ievadi bāzes punktus: "))
reizinatajs2 = float(input("Ievadi reizinātāju: "))
kopa2 = punkti2 * reizinatajs2
print(vards2, "ieguva", kopa2, "punktus")


print("kopā", vards, "un", vards2, "ieguva", kopa + kopa2, "punktus")