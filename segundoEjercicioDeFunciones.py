#segundo ejercicio de funciones 
def dibujar(altura,anchura,caracter):
    for i in range(altura):
        for j in range(anchura):
            print(caracter," ",end=" ")
        print()   
    

altura = int()
anchura = int()

altura = int(input("Ingrese la altura de la matriz \n"))
anchura = int(input("Ingrese la anchura de la matriz \n"))
caracter = input("Ingrese el caracter de la matriz \n")

dibujar(altura,anchura,caracter)
