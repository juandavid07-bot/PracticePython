#Ejerccio de funciones 

def dibujar_rectangulo(A,a):
    for i in range(A):
        for j in range(a):
            print("*",end="")# De igual forma, podemos usar este valor personalizado del parámetro end para mostrar los valores de un iterable en la misma línea:
        print()
    


altura = int()
anchura = int()

altura=int(input("ingrese el valor de la altura del rectangulo \n"))
anchura=int(input("ingrese el valor de la anchura del rectangulo \n"))

dibujar_rectangulo(altura,anchura)

print(type(altura),type(anchura))





