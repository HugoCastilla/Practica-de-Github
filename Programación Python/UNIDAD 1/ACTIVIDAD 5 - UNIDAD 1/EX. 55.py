#Última vez que reutilizamos el mismo código, lo prometo. A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

sum=0
vec=0
totsum=0

while totsum<=50:
    vec=vec+1
    num1=int(input("introduce un número: "))
    num2=int(input("introduce otro número: "))
    sum=num1+num2
    print(f"La suma de ambos números es: {sum}")
    totsum=totsum+sum
    print(f"La suma de sumas actual es: {totsum} y llevas {vec} repeticiones.")

print("Programa finalizado.")
print("La suma de todas las sumas es", totsum,". El total de repeticiones es", vec)