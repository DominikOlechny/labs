import random
x = int(input("podaj liczbe elemtow"))
lista1 = []
for i in range(x):
        n = random.randint(1, 10)
        lista1.append(n)
print(lista1)
x2 = int(input("podaj liczbe elemtow"))
lista2 = []
for i in range(x2):
        n2 = random.randint(5, 15)
        lista2.append(n2)
print(lista2)
x3 = int(input("podaj licz"))
if x3 in lista1:
    print("wystepuje")
elif x3 in lista2:
    print("liczb wystepuje w lista2")
else:
    print("nie ma w obu")