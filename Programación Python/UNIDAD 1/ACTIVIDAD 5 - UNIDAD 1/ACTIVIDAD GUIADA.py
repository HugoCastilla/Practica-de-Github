import random

num=random.randint(1,20)
intentos=3
print("Te quedan", intentos, "intentos.")
numero=int(input("Introduce un número del 1 al 20: "))

while num!=numero:
    if numero<1 or numero>20:
        print("Ese número no cumple las condiciones indicadas.")
        intentos=intentos-1
        numero=int(input("Vuelve a introducir un número: "))
        print("Te quedan", intentos, "intentos.")
    else:
        if intentos==0:
            break
        else:
            print("Has introducido el número", numero, ", no has acertado.")
            intentos=intentos-1
            numero=int(input("Vuelve a introducir un número: "))
            print("Te quedan", intentos, "intentos.")
else:
    print("¡Has acertado!")
print("Fin del programa")