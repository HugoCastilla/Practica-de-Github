#Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario tenga x oportunidades para ver si letra introducida está en esa palabra.

palabra=input("Introduzca una palabra: ")
intentos=len(palabra)

for i in range (intentos):
    letra=input("Introduzca la letra que creas que está en la palabra: ")
    if letra in palabra:
        print(f"La letra {letra} se encuentra en la palabra.")
    else:
        print(f"La letra {letra} no se encuentra en la palabra.")
    intentos=intentos-1
    print(f"Te quedan {intentos} intentos.")