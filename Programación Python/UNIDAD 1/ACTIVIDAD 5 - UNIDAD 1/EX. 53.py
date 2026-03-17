# A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While

res="s"
sum=0
vec=0
totsum=0

while res=="s":
    vec=vec+1
    num1=int(input("introduce un número: "))
    num2=int(input("introduce otro número: "))
    sum=num1+num2
    print(f"La suma de ambos números es: {sum}")
    totsum=totsum+sum
    res=str(input("Deseas repetir la operación (s/n): "))

print("Programa finalizado.")
print("La suma de todas las sumas es", totsum,". El total de repeticiones es", vec)
