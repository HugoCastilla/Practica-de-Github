# Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random
inen=0
num=random.randint(1,5)
intent=3
while intent>0:
    inen=int(input("Intenta adivinar el número (1-5): "))
    if num==inen:
        print("¡Has acertado el número!")
        break
    if num>=6 or num<=0:
        print("Ese número no entra entre el 1 y el 5.")
    if num!=inen:
        print("Número incorrecto.")
    intent=intent-1
    if intent==0:
        print("Te has quedado sin intentos.")
        break
print("Programa finalizado.")