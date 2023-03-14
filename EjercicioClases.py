## EjercicioClases
"""
Escribir una clase en python que convierta un número entero a número romano

"""
import math

class comvertidor: #asi se indica la clase 
   def  __init__(self,num):
        self.num = num  #el uso self es de uso obligatorio si se quiere crear una clase que tenga un constructor se le tiene que pasar self 
       # self.full_name = f"{num})" # Parametro publico 
        self.__name = num # Parametro privada 
        #19self.Tamaño=len(num)

   def Numer(self): # se pasa self podemos acceder todo lo que esta guradado en self 
        #print(f"{self.full_name} Esta caminando") # asi accedemos a los datos de self 
          Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
          Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
          Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
          N=self.num
          u= N % 10
          print(u)
          d=int(math.floor(N/10))%10
          print(d)
          c=int(math.floor(N/100))
          print(c)
          if(N>=100): 
               respuesta=Centena[c]+Decena[d]+Unidad[u]
          elif(N>=10):
               respuesta=Decena[d]+Unidad[u]
          else:
               respuesta=Unidad[N]
          return respuesta

    

my_persom = comvertidor(19)
##print(my_persom.num)
print(my_persom.Numer())

