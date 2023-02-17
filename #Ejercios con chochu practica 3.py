#Ejercios con chochu practica 3
server = [25,6,7,2,8,32]
serverPares = []
serverInpares = []
for i in server:
    if i % 2!= 0:
        serverInpares.append(i)
    else:
        serverPares.append(i)

print(server)
print(serverPares)
print(serverInpares)