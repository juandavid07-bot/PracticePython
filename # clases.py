# clases 
#realiza una tarea concreta, una clase responde a una logica a un objeto

class EmptyPerson: #asi se indica la clase 
    pass # se coloca este cuando este vacio 

class Person: # esta persona esta en la capacidad de recibir algo 
    def  __init__(self,name,surname,alias="sin alias"):
        self.name = name  #el uso self es de uso obligatorio si se quiere crear una clase que tenga un constructor se le tiene que pasar self 
        self.surname = surname # self se refiere a el mismo, se refiere a la instacia de persona en este caso 
        self.full_name = f"{name} {surname} ({alias})" # Parametro publico 
        self.__name = name # Parametro privada 
    
    def walk(self): # se pasa self podemos acceder todo lo que esta guradado en self 
        print(f"{self.full_name} Esta caminando") # asi accedemos a los datos de self 

my_persom = Person("Juan","Montenegro")
print(my_persom.name)
my_persom.walk()

my_other_person = Person("Edilberto", "Niño","perro")
my_other_person.walk()
my_other_person.full_name = " Hector leon el loco sapo triple hp"
print(my_other_person.full_name) # no se accede al constructor debido a que se cambio el objeto, el constructor solo es para crear el objeto 