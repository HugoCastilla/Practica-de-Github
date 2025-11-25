#Programa que sume los n primeros números naturales. n lo introduce el usuario.
num=int(input("Introduce un número entero positivo: "))

if num>0:
    suma = num*(num + 1)//2
    print(f"La suma de los primeros {num} números naturales es: {suma}")
else:
    print("Por favor, introduce un número entero positivo.")