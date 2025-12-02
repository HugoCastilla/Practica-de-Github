#Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random
inen=0
num=random.randint(1,5)
while inen!=num:
    inen=int(input("Intenta adivinar el número (1-5): "))
    if num==int:
        break
    elif num>=6 or num<=0:
        print("Ese número no entra entre el 1 y el 5.")
    else:
        print("Número incorrecto.")
print("¡Has acertado el número!")