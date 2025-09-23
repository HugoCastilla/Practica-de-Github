#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math

diam=float(input("Introduce el diámetro del círculo: "))
radio=diam/2

peri=(2*math.pi)*radio
are=math.pi*(radio**2)

perimetro=round(peri, 1)
area=round(are, 1)

print("El perímetro del círculo es", perimetro)
print("El área del círculo es", area)
