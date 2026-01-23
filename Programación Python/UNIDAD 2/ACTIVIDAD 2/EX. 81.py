#Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra
import random
lista1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
valor_azar=random.choice(lista1)
adivinado=False
while not adivinado:
    intento=input("Adivina la letra seleccionada al azar de la lista: ")
    if intento==valor_azar:
        print("¡Correcto! Has adivinado la letra.")
        adivinado=True
    else:
        print("Incorrecto. Inténtalo de nuevo.")