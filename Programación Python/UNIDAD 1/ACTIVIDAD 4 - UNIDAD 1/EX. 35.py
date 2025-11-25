#Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre

palabra=input("Introduce una palabra: ")
num=int(input("Introduce el número de repeticiones: "))

for _ in range(num):
    print(palabra)