#Ejercico con chochu 4
from itertools import count

import random


solu = []
rep = []


for i in range (5):
    solu.append(random.randrange(1,10))
print(solu)
for i in solu:
    if(solu.count(i)) >1:
        rep.append(i)

print(rep)
