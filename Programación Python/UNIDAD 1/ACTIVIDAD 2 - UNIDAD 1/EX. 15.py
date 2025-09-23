# Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math

radio=float(input("Introduce el radio del cilindro: "))
altura=float(input("Introduce la altura del cilindro: "))

areaus=2*math.pi*radio*(radio + altura)
volum=math.pi*(radio**2)*altura

area=round(areaus, 2)
volumen=round(volum, 2)

print("El área del cilindro es", area)
print("El volumen del cilindro es", volumen)