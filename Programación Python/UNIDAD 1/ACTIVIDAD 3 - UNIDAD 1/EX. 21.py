#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math

a=int(input("Introduce el valor de a: "))
b=int(input("Introduce el valor de b: "))  
c=int(input("Introduce el valor de c: "))
discriminante=(b**2)-(4*a*c)

if discriminante<0:
    print("La raíz cuadrada de un número negativo no existe.")
else:
    x1= (-b-math.sqrt(discriminante))/(2*a)
    x2= (-b+math.sqrt(discriminante))/(2*a)
    
    print(f"El valor de x1 es: {x1} y el valor de x2 es: {x2}.")

