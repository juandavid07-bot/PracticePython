#Ejercicio de hatty potter 
my_questions = ["Do you like Dawn or Dusk? :\n 1) Dawn \n  2) Dusk \n" ,

"When I’m dead, I want people to remember me as: \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold \n",

"Which kind of instrument most pleases your ear? : \n 1) The violin \n 2) The trumpet \n  3) The piano \n 4) The drum \n"]
requests = []
Gryffindor =  0
Ravenclaw = 0
Hufflepuff =  0
Slytherin = 0

for my_question in my_questions:
    res = input(my_question)
    requests.append(res)

for i in range (len(requests)):
    if i == 0:
        if requests[i] == '1':
         Gryffindor = Gryffindor + 1
         Ravenclaw = Ravenclaw + 1
        if requests[i] == '2':
         Hufflepuff = Hufflepuff + 1
         Slytherin = Slytherin + 1
    if i == 1:
        if requests[i] == '1':
         Gryffindor = Gryffindor + 1
        if requests[i] == '2':
         Ravenclaw = Ravenclaw + 1
        if requests[i] == '3':
         Hufflepuff = Hufflepuff + 1
        if requests[i] == '4':
         Slytherin = Slytherin + 1
    if i == 2 :
        if requests[i] == '1':
            Slytherin = Slytherin + 1
        if requests[i] == '2':
            Hufflepuff = Hufflepuff+ 1
        if requests[i] == '3':
            Ravenclaw = Ravenclaw + 1
        if requests[i] == '4':
            Gryffindor = Gryffindor + 1
            

print(requests,Gryffindor,Slytherin,Hufflepuff,Ravenclaw)
if Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
 print(" la casa con mas puntos es Gryffindor con un total de ", Gryffindor)
elif Hufflepuff > Gryffindor  and  Hufflepuff > Slytherin  and Hufflepuff > Ravenclaw:
 print(" la casa con mas puntos es Hufflepuff con un total de ", Hufflepuff)
elif Ravenclaw > Gryffindor  and  Ravenclaw > Slytherin  and Ravenclaw > Hufflepuff :
 print(" la casa con mas puntos es Ravenclaw con un total de " , Ravenclaw)
elif Slytherin > Gryffindor  and  Slytherin > Ravenclaw  and Slytherin > Hufflepuff :
 print(" la casa con mas puntos es Slytherin con un total de " , Slytherin)



