#Ejercicio de año Bisiesto 
def bisesto(año):
    if ((año%4 ==0 and año%100!=0 )or año%400==0):
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")




año = int(input("Digite un año para saber si es bisiesto o no : \n"))
bisesto(año)