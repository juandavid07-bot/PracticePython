 #Magic ball 8
import random 

ball = ["Yes - definitely","It is decidedly so","Without a doubt","Reply hazy, try again","Ask again later","Better not tell you now","My sources say no","Outlook not so good","Very doubtful"]
quiestion = str()
num = random.randint(0,8)

quiestion = input("Pregunta lo que quieras")

print(ball[num])
