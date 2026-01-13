import random
quier1=0

print("Hola, mi nombre es Tristán 1.0.1")
name=str(input("¿Cual es tu nombre?  "))
print("")
print(f"Encantado, {name}.")
juego1=str(input("¿Quieres que juguemos un juego? (S/N) "))

num=random.randint(1,10)
while quier1!="N":
    if juego1=="S":
        guess=int(input("Intenta adivinar el número del 1 al 10: "))
        if num==guess:
            print("")
            print("¡Has acertado el número!")
            break
        else:
            quier1=str(input("Incorrecto. ¿Quieres probar otra vez? (S/N) "))
            if quier1=="N":
                break
            elif quier1=="S":
                quier1="S"
    else:
        break
print("")
print("Bueno, se me ocurre otra cosa que podemos hacer.") 
juego2=str(input("¿Quieres jugar al ahorcado? (S/N) "))
if juego2=="S":
    print("hi")
elif juego2=="N":
    print("Niggers")
else:
    print("Repite porfa")


