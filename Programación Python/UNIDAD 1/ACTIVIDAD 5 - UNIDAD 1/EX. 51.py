# A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While

veces=int(input("Introduce el número de repeticiones: "))

while veces>0:
    print("¡Buenos días!")
    veces=veces-1