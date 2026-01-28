import random
quier1=0
listahorcado=["plátano", "niño", "balón", "comedor", "calcetín", "padre", "#!@~/€%&*^!", "agua", "café", "aigua", "zumo", "autismo", "enfermeda", "espacio", "zarigüeya"]
ahorca=""
letra=""
juego2="s"
print("Hola, mi nombre es Tristán 1.0.1")
name=str(input("¿Cual es tu nombre?  "))
print("")
print(f"Encantado, {name}.")
juego1=str(input("¿Quieres que juguemos un juego? (s/n) ")).lower()

num=random.randint(1,10)
while quier1!="n":
    if juego1=="s":
        guess=int(input("Intenta adivinar el número del 1 al 10: "))
        if num==guess:
            print("")
            print("¡Has acertado el número!")
            break
        else:
            quier1=str(input("Incorrecto. ¿Quieres probar otra vez? (s/n) ")).lower()
            if quier1=="n":
                break
            elif quier1=="s":
                quier1="s"
    else:
        break
print("")
print("Bueno, se me ocurre otra cosa que podemos hacer.") 
juego2=str(input("¿Quieres jugar al ahorcado? (s/n) ")).lower()
if juego2=="s":
    while juego2!="s":
        ahorcado=random.choice(listahorcado)
        for i in len(ahorcado):
            ahorca=ahorca+" _ "
        print(ahorca)
        print(ahorcado)
        letra=str(input("Introduce una letra: "))
else:
    if juego1 and juego2=="n":
        print("Vaya. Parece que hoy no tenemos ganas de jugar, ¿eh?")
    else:
        print("")
print("Déjame un momento para que piense lo que podemos hacer ahora.")



    


