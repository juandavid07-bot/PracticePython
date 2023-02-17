#Diccionarios

my_dicc = dict() #como se declara un diccionario 
other_dic = {} # otra forma como se declara un diccionario 
my_dicc = {"Nombre": "Juan","edad": "23","clave":"12345"}

other_dic = {
    "Nombre" : "Juna",
    "Apellido" : "Montenegro",
    "Edad": "23",
    "Lengiajes": {"Python","java","c#"},
    1 : 1.284
}

my_dicc["Nombre"]="David" # Forma de actualizar un elemento 
my_dicc["calle"] = "caras656"

print(my_dicc)

del my_dicc["calle"]
print(my_dicc)

print("Juna" in other_dic)# no busca por el valor si no el campo como se ve en la siguiente linea 
print("Nombre" in other_dic)
print(other_dic["Nombre"]) # Esta es la forma de mostrar el valor del campo nombre 

print(other_dic.fromkeys(("Nombre",1)))# se crea un diccionario nuevo sin valores 


