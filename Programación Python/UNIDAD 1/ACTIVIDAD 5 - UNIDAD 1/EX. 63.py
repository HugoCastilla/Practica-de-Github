#Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número

import random
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0

for i in range(100):
    num=random.randint(1,6)
    if num==1:
        uno=uno+1
    if num==2:
        dos=dos+1
    if num==3:
        tres=tres+1
    if num==4:
        cuatro=cuatro+1
    if num==5:
        cinco=cinco+1
    if num==6:
        seis=seis+1

print("Uno:", uno)
print("Dos:", dos)
print("Tres:", tres)
print("Cuatro:", cuatro)
print("Cinco:", cinco)
print("Seis:", seis)
