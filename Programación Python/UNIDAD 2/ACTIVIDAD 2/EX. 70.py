#Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.

num=int(input("Introduce una cantidad de palabras: "))

lista1=[]
lista2=[]

for i in range(num):
    palabra=input("Introduce una palabra: ")
    lista1.append(palabra)
    lista2.append(palabra)

lista2.reverse()
print(lista1)
print(lista2)
