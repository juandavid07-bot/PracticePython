#Proyecto Final De practica 
yuan=float(input("What do you have left in yuan?"))
yen=float(input("What do you have left in yen?"))
won=float(input("What do you have left in won?"))

var = yuan*0.15
var = var + (yen*0.0078)
var = var + (won * 0.0078)

print("El valor es:", var)
