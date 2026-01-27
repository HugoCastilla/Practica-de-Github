#Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente. Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe algún método que permita sumar el contenido de una lista?
import random
lista1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
total=0
partidas=0
jugar=True
while jugar:
    valorrandom=random.choice(lista1)
    adivinado=False
    intentos=0
    while not adivinado:
        intento=input("Adivina la letra seleccionada al azar de la lista: ")
        intentos+=1
        if intento==valorrandom:
            puntos=8-intentos+1
            print(f"¡Correcto! Has adivinado la letra. Puntos obtenidos: {puntos}")
            total+=puntos
            partidas+=1
            adivinado=True
        else:
            print("Incorrecto. Inténtalo de nuevo.")
    respuesta=input("¿Quieres jugar de nuevo? (s/n): ")
    if respuesta.lower()!='s':
        jugar=False    
