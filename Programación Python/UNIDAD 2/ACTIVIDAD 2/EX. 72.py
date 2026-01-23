#A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista

seguir = "S"
lista = []

while seguir == "S":
    letra = input("Introduce una letra: ").lower()

    if letra == "á":
        letra = "a"
    elif letra == "é":
        letra = "e"
    elif letra == "í":
        letra = "i"
    elif letra == "ó":
        letra = "o"
    elif letra == "ú":
        letra = "u"

    if letra.isalpha() and len(letra) == 1:
        if letra not in lista:
            lista.append(letra)
            print("Lista actual:", lista)
        else:
            print("Esa letra ya está en la lista.")
    else:
        print("Error. Debes introducir una letra.")

    seguir = input("¿Quieres introducir otra letra? (S/N) ")

print("Programa finalizado.")
