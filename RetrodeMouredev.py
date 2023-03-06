# * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
# * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# * NO hace falta comprobar que ambas palabras existan.
# * Dos palabras exactamente iguales no son anagrama.

# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def anagrama(palabra1, palabra2):
    bol = True
    # Convertimos ambas a minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    # Luego convertimos las cadenas a arreglos, porque vamos a ordenarlas pero es más sencillo ordenar un arreglo
    palabra1_arreglo = list(palabra1)
    palabra2_arreglo = list(palabra2)
    # Las ordenamos
    palabra1_arreglo.sort()
    palabra2_arreglo.sort()
    # Convertir de vuelta a cadena
    palabra1_ordenada = "".join(palabra1_arreglo)
    palabra2_ordenada = "".join(palabra2_arreglo)
    # Y finalmente comprobar si son iguales
    if palabra1_ordenada == palabra2_ordenada:
        bol = True
    else:
        bol = False
    return bol

string = str(input("Ingrese una palabra string \n"))
string2 = str(input("Ingrese una palabra string \n"))
if string != string2:
    res = anagrama(string,string2)
    print(res)