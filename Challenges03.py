# Es un numero primo 
""""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""
def es_primo():
    
    for i in range(1,101):
        bol=False
        for j in range(2,i):
            if  j!=i:
                if i%j ==0:
                    bol=True
        if bol == True:
         print(i,"No es un numero primo")
        else:
         print(i,"Es un numero primo")
def prueba(l):
    bol=False
    for index in range(2,l):
        nex = index+1
        print("val:",index)
        if  index != l:
            if l%index ==0:
                bol = True
    if bol == True:
        print(l,"No es un numero primo")
    else:
        print(l,"Es un numero primo")
        

es_primo()
#prueba(7)
