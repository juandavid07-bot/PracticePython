#Cuantos años bisestos hay

def calculo(primerA,SegundoA):
    can =  SegundoA - primerA
    cont = 0
    for i in range(primerA,SegundoA+1):# ASI SE RECORRE UNOS VALORES PREDETERMINADOS range(MAX,MIN,PASOS)
        if((i%4==0 and i %100!=0) or i%400==0):
            cont +=1
    print("De",primerA ,"a",SegundoA, "hay",can, "años,",cont,"de ellos bisiestos.")


primerA = int(input("Ingrese un año :"))
SegundoA = int(input("Ingrese un año posterior al año anterior :"))

if SegundoA > primerA:
    calculo(primerA,SegundoA)
else:
    print("el segundo año codificado es menor al primer año, intentelo denuevo ")