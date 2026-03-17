#Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural. Con While

sum=0
totsum=0

while totsum<=50:
    num1=int(input("introduce un número: "))
    num2=int(input("introduce otro número: "))
    sum=num1+num2
    print(f"La suma de ambos números es: {sum}")
    totsum=totsum+sum
    print(f"La suma de sumas actual es: {totsum}")

print("Programa finalizado.")
print("La suma de todas las sumas es", totsum,".")