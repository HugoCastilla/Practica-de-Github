#Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.

import random
inen=0
num=random.randint(1,1000)
while num!=inen:
    inen=int(input("Intenta adivinar el número (1-1000): "))
    if num==inen:
        print("¡Has acertado el número!")
    elif num>=1001 or num<=0:
        print("Ese número no entra entre el 1 y el 5.")
    else:
        if num>inen:
            print("Has introducido un número menor.")
        if num<inen:
            print("Has introducido un número mayor.")
print("Programa finalizado.")