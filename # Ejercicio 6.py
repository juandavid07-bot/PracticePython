# Ejercicio 6 
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aporbadas = []
repobadas = []
cont = int(0)
for materia in materias:
    cont = cont + 1
    notas = float(input("Cual es la nota : " + materia ))
    if notas >= 50:
        aporbadas.append(materia)
    else:
        repobadas.append(materia)
for j in range (len(repobadas)):
    print("materias que tiene que repetir", repobadas[j])   