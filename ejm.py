def es_bisiesto(t):
    return t % 400 == 0 or (t % 100 != 0 and t % 4 == 0)

print("Contador de años bisiestos")
inicio = int(input("Escriba un año: "))
print("Escriba otro año posterior a", str(inicio) + ": ", end="")
final = int(input())
while final < inicio:
    print(final, "no es mayor que", str(inicio) + ". Inténtelo de nuevo: ",
          end="")
    final = int(input())

contador = 0
for i in range(inicio, final + 1):
    if es_bisiesto(i):
        contador += 1

print("De", inicio, "a", final, "hay", final - inicio + 1, "años,",
      contador, "de ellos bisiestos.")