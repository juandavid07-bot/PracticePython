#Ejercicio con Chochu 2
from pickle import TRUE
import string


n = int()
list = []
lista_entero = []
lista_string = []
n = int(input("Ingrese un valor para la lista :"))

for i in range(n):
    list.append(input("ingresa un valor al areglo :"))

for i in list:
     if i.isdigit() : 
        lista_entero.append(i)
     else:
        lista_string.append(i)

#     print(var)
    
print(list)
print(lista_entero)
print(lista_string)