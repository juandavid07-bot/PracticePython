#Ejecicio 4
import random
n = int()
lista = list()
for i in range (10):
    n = random.randint(1, 11)
    lista.append(n)
lista.sort(reverse=True)
print(lista)
