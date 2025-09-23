 #Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
import math

sqrt_num=float(input("Introduce un número para calcular su raíz cuadrada: "))
raiz=math.sqrt(sqrt_num)
division=raiz//2

raiiz=round(raiz, 1)
diviision=round(division, 1)

print("La raíz cuadrada es:", raiiz)
print("La división es:", diviision)