#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra

palabra=input("Introduce una palabra: ")
num=-1

for i in range (len(palabra)):
    letra=palabra[i]
    print(f"La letra {i+1} es {letra}.")