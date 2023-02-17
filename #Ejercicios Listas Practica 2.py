#Ejercicios Listas Practica 2



materias = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
notas = list()
aux = str()
tamaño = int()
for materia in materias:
    print("Cuanto saco en :",materia)
    aux = input()
    notas.append(aux)

tamaño= len(materias)
#print(tamaño)
for i in range (len(materias)):
   print("La nota de la materia", materias[i],"es:",notas[i])