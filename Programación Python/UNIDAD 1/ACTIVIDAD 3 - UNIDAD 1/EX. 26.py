#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

Letra=input("Introduce una letra (mayúscula o minúscula): ")

if Letra.isupper()==True:
    print("La letra está en mayúscula.")
elif Letra.islower()==True:
    print("La letra está en minúscula.")
else:
    print("No es una letra.")
