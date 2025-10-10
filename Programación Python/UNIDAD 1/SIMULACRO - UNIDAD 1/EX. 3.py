import math

formato=input("¿Cómo quiere el resultado?(mayúsculas/minúsculas): ")
radio=float(input("Introduzca el radio del cilindro: "))
altura=float(input("Introduzca la altura del cilindro: "))

volumen=(math.pi * radio**2)*altura

if formato=="mayúsculas":
    print("EL VOLUMEN DEL CILINDRO ES:", round(volumen, 3))
elif formato=="minúsculas":
    print("el volumen del cilindro es:", round(volumen, 3))
else:
    print("Error. No ha introducido el formato correcto.")