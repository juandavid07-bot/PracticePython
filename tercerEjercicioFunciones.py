#Tecer ejercicio de funciones 
def dibujar1(anchura):
    for i in range (anchura):
        for j in range(i):
            print("* ",end=" ")
        print()

        


def dibujar2(anchura):
   for i in range(anchura,0,-1) : # con este metodo podemos recorrer al rever un ciclo for 
     for j in range(i,0,-1):
        print("* ",end=" ")
     print()

anchura = int(input("Anchura del triángulo: \n"))

dibujar1(anchura)
dibujar2(anchura)
