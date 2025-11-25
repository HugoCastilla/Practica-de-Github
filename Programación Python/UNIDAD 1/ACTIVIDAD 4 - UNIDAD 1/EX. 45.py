# Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
import string
noletra=0

varvoc=""
varcon=""

vocal="aeiouáéíóú"
consonante="bcçdfghjklmnpqrstvwxyz"

palabra=input("Introduce una palabra: ")
palabra=palabra.lower()
for i in range(len(palabra)):
    if palabra[i] in vocal:
        varvoc=varvoc+palabra[i]
    elif palabra[i] in consonante:
        varcon=varcon+palabra[i]
    else:
        noletra=noletra+1

print(f"Las vocales de la palabra son: {varvoc}")
print(f"Las consonantes de la palabra son: {varcon}")
print(f"Hay {noletra} carácteres que no son letras en la palabra.")
