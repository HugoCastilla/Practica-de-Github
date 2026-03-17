#Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados: a. Cantidad total de valores b. Cantidad de números c. Cantidad de letras d. Cantidad de mayúsculas e. Suma de los valores numéricos

lista1=['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
total=len(lista1)
numeros=0
letras=0
mayusculas=0
suma_numeros=0

for x in lista1:
    if x.isdigit():
        numeros+=1
        suma_numeros+=int(x)
    elif x.isalpha():
        letras+=1
        if x.isupper():
            mayusculas+=1

print("Cantidad total de valores:", total)
print("Cantidad de números:", numeros)
print("Cantidad de letras:", letras)
print("Cantidad de mayúsculas:", mayusculas)
print("Suma de los valores numéricos:", suma_numeros)
