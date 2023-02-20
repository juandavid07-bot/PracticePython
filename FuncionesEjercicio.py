def lista(n):
    lista=[]
    for j in range(n):
        print("Dígame la palabra",(j+1))
        val = input()
        lista.append(val)
    return lista
print("Generador de listas\n")
lis = int()
while lis <= 0:
    lis = int(input("¿Cuántas listas quiere escribir?\n"))
principal=[]
for i in range(lis):
    print("Dígame cuántas palabras tiene la lista",(i+1),": \n")
    num =int(input())
    respue= lista(num)
    principal.append(respue)
for n in range(len(principal)):
    print("La lista",(n+1),"es :",principal[n])