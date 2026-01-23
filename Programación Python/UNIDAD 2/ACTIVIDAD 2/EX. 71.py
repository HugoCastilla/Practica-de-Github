#Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
seguir="S"
lista=[]
while seguir=="S":
    letra=input("Introduce una letra: ")
    if letra not in lista:
        if letra.isalpha():
            lista.append(letra)
            print("Lista actual:", lista)
        else:
            print("Error. Ese carácter no es una letra.")
    else:
        print("Esa letra ya está en la lista o no es una letra.")
    seguir=input("¿Quieres introducir otra letra? (S/N) ")
print("Programa finalizado.")
