#A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.
import string
palabra=input("Introduzca una palabra: ")
intentos=len(palabra)

for i in range (intentos):
    letra=input("Introduzca la letra que creas que está en la palabra: ")
    if letra in palabra.lower():
        print(f"La letra {letra} se encuentra en la palabra.")
        for let in range(len(palabra)):
            if letra in palabra[let]:
                print("La letra se encuentra en la posición",let+1 )
    else:
        print(f"La letra {letra} no se encuentra en la palabra.")
    intentos=intentos-1
    print(f"Te quedan {intentos} intentos.")