#Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
numeros=0
numeros=int(input("Introduce una cantidad de números: "))

lista=[]

for i in range(numeros):
    lista.append(input("Introduce un número: "))

print(list(set(lista)))

