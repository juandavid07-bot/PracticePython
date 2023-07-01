"""
Escribir una función que reciba una frase y
devuelva un diccionario con las palabras que contiene y su longitud.

"""

def Frase(frase):
    val = frase.split(" ")
    my_dicc = dict()
    for i  in range (len(val)):
        my_dicc[val[i]]=len(val[i])
        print(val[i])
    print(my_dicc)
"""  my_dicc = dict()
    gazpacho['Aceite'] = '300 ml'
    print()
"""

frase="El perro está jugando en el parque"
Frase(frase)