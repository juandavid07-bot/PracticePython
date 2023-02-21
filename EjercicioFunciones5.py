def lista(n):
    lista=[]
    for j in range(n):
        print("Dígame la palabra",(j+1))
        val = input()
        lista.append(val)
    return lista

def Eliminar(num,L):
    lista2=[]
    for j in range(num):
        print("Dígame la palabra",(j+1))
        val2 = input()
        lista2.append(val2)
    print("La lista de palabras a eliminar es: ",lista2)
    for l in lista2:
        for ju in range  (len(L)-1,-1,-1): # el -1,-1,-1 es para que no presente este error list index out of range
            if L[ju] == l:
              del(L[ju])# se eliminan los elemnetos repetidos a diferencia que el remove()
    return L
print("Generador de listas\n")
lis = int()
lis2 = int()
while lis <= 0:  
     print("Dígame cuántas palabras tiene la lista : \n")
     lis = int(input())
List=lista(lis)
print("La lista creada es: ",List)
while lis2 <= 0:  
     print("Dígame cuántas palabras tiene la lista de palabras a eliminar \n")
     lis2 = int(input())
List2 = Eliminar(lis2,List)
print("La lista es ahora: ",List2)