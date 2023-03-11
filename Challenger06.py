"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.

"""
def conteo(Lis):
    ejm="j"
    Lista=list()
    cont=0
    Repetidos =list()
    print(ejm.isalpha())
    for i in Lis.split():
        Lista.append(i)
    num = len(Lista)
    for j in range(num):
        palaba1 = Lista[j].lower()
        palaba1 = palaba1.replace(".","").replace(",","").replace(":","")
        if palaba1 not in Repetidos:
            for x in range(j+1,num):
                palaba2 = Lista[x].lower()
                palaba2 = palaba2.replace(".","").replace(",","").replace(":","")
            #   print("Letra : ",palaba1)
            #    print(palaba2)
                if(palaba1== palaba2 and j != x ):
                    cont +=1
                    if palaba1 not in Repetidos:
                        Repetidos.append(palaba1)
            print("El numero de veces que se repitio fueron:",cont,":",palaba1)
            cont=0
    print("------------------------------------------------------------")
    print(Repetidos)
"""   
            if(palaba1== palaba2 and j != x and palaba2 not in Repetidos ):
                cont +=1
                print("El numero de veces que se repitio fueron:",cont,":",palaba1)
        Repetidos.append(palaba1)
       cont=0"""
        
def imprimir(l):
    for i in l.split():
        print(i)

conteo("Hola, Hola, hola mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev). brais")