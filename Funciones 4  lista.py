def Funcion(D):
    lista = []
    for i in range(D):
        val = input("Dígame la palabra:")
        lista.append(val)
    return lista

Digitos = int(input("Dígame cuántas palabras tiene la lista:"))

Respuesta= Funcion(Digitos)

print(Respuesta)