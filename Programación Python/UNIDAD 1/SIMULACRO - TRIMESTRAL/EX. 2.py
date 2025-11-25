sumpos=0
sumneg=0
cien=0

for i in range(7):
    num=int(input("Introduce un número: "))
    if num>0:
        sumpos=sumpos+num
    else:
        sumneg=sumneg+num
    if num>=100:
        cien=cien+1

print(f"La suma de los números positivos es: {sumpos}")
print(f"La suma de los números negativos es: {sumneg}")
print(f"Números mayores o iguales a 100: {cien}")
