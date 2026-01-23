#A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.
import random
lista1=['zapatos', 'coco', 'pantalon', 'cebolla', 'canelones', 'bufanda', 'sinvergüenza', 'calcetines', 'medalla', 'autopista']
valorrandom=random.choice(lista1)
letras=list(valorrandom)
random.shuffle(letras)
palabra=''.join(letras)
print("Palabra desordenada:", palabra)
intentos=3
adivinado=False
while intentos>0 and not adivinado:
    intento=input(f"Tienes {intentos} intentos restantes. Adivina la palabra: ")
    if intento==valorrandom:
        print("¡Correcto! Has adivinado la palabra.")
        adivinado=True
    else:
        intentos-=1
        print("Incorrecto. Inténtalo de nuevo.")
if not adivinado:
    print(f"Lo siento, has agotado tus intentos. La palabra correcta era: {valorrandom}")