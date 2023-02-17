#Sets

myset = {"Ejm","plo"}
myotherset = {"Juan","Montenegro",23} #se declara con las llaves llenas para declararlo de otra forma 
print(type(myset))
myotherset.remove(23)
my_list = list(myotherset) #Dependiendo por que no sabemos el orden del set

myset = myset.union(myotherset)
print(myset)