#A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo

lista1=['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
letras=[]
numeros=[]
for x in lista1:
    if x.isdigit():
        numeros.append(x)
    elif x.isalpha():
        letras.append(x)
orden=input("¿Quieres ordenar ascendente (A) o descendente (D)? ")
if orden=="A":
    letras.sort(key=str.lower)
    numeros.sort()
elif orden=="D":
    letras.sort(key=str.lower, reverse=True)
    numeros.sort(reverse=True)

print("Letras ordenadas:", letras)
print("Números ordenados:", numeros)   