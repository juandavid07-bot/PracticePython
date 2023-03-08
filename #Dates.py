#Dates

def impri_fecha(date):
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.year)
    print(date.month)
    print(date.timestamp())

from  datetime import datetime 

now = datetime.now()#nos va inicializar un objeto 
#Acceso a las horas de o crear una fecha inicializada cuando se ejecute el cotigo 

#esta es una representaion unica de un tiempo con esto se puede inferir a una fecha este es el formato posics
timestamp = now.timestamp()
print(timestamp)
print("------")
print(now.day,"/",now.month,"/",now.year)
print("------")
year_2024 = datetime(2024,1,1,3)# se define una fecha futura para crear una nueva fecha, lo minimo que tenemos que enviar 
# es el año el mes y el dia
impri_fecha(year_2024)

from  datetime import time # time es un obejto que no tiene nada sobre time se tiene que lanzar operaciones para 
# acceder a esos datos, es un objeto para encapsular tiempo 

current_time = time(21,6,0)
print(current_time.hour)
print(current_time.min)
print(current_time.minute)
print(current_time.second)

from  datetime import date 

current_date = date.today() # se define el objeto de la siguiente manera con el dia actual 
print(current_date.year)
print(current_date.day)
print(current_date.month)

current_date = date(current_date.year,current_date.month+1,current_date.day) #asi se aumenta o modifica el valor
print(current_date)
dif = year_2024 - now #diferencias de dos dias 
print(dif)
dif = year_2024.date() - current_date #diferencias de dos dias 
print(dif)
print("------------------------")

from datetime import timedelta #sirve para operar entre fechas 
time_delta = timedelta(200,100,1000,weeks=10)# dias , segundos , microsegundos,semanas
end_delta= timedelta(300,100,1000,weeks=13)# dias , segundos , microsegundos,semanas

print(end_delta+time_delta)
print(end_delta-time_delta)