def creciente(ancho):
    for i in range(1, ancho + 1):
        for j in range(i):
            print("* ", end="")
        print()

def decreciente(ancho):
    for i in range(1, ancho):
        for j in range(ancho - i):
            print("* ", end="")
        print()

anchura = int(input("Anchura del triángulo: "))
for i in range(anchura, 0, -1):
    creciente(i)
    decreciente(i)