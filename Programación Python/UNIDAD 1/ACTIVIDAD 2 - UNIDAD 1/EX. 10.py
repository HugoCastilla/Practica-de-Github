#Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
num1=float(input("Introduce el dividendo: "))
num2=float(input("Introduce el divisor: "))

cociente=round(num1/num2,0)
resto=num1%num2

print("El cociente de la división es", cociente)
print("El resto de la división és", resto) 
if num1 % 2 == 0:
    print(f"El dividendo {num1} es par.")
else:
    print(f"El dividendo {num2} es impar.")