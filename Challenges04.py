# Challenge04
"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def cadena(t):
    Aux=[]
    respuesta = str
    for i in range(len(t)):
        print(t[-i-1])
        Aux.append(t[-i-1])
    respuesta="".join(Aux) # Forma de añadir o comvertir una lista a cadena
    print(respuesta)

text=input()
cadena(text)