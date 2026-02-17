pos=0
neg=0
cien=0

for i in range(7):
    num=int(input("Ingrese un numero: "))
    if num>=00:
        pos=pos+num
    else:
        neg=neg+num
    if num>100:
        cien=cien+1
    
print("La suma de los numeros positivos es:",pos)
print("La suma de los numeros negativos es:",neg)
print("La cantidad de numeros mayores a 100 es:",cien)