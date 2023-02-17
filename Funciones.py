# Funciones 

def my_function ():
    print("Esto es un mesaje que llama a una funcion")

my_function()#se llama asi la funcio del main
my_function()
my_function()

def mult_lo(num1 : int ,num2 : int): # se puede declara las variables 
    print(num1+num2)

mult_lo(1.7,5.5) # Concatena los dos valores si son un string 
mult_lo(1,5) # Concatena los dos valores si son un string 
mult_lo(1564,5595) # Concatena los dos valores si son un string 
mult_lo("1","65") # Concatena los dos valores si son un string 

def sum_2_valores_retorna(num1 : int ,num2 : int): # funcion retorna algo
    resultado = num1+num2 
    return resultado

resultado = sum_2_valores_retorna(10,5)


def print_text(*texts): # lista de elementos infinita 
    for text in texts:
        print(text.upper())
print_text("hola","como","estas","?")
