# Crea un programa que cuente todos los números pares hasta el número 50

pares=0
impares=0

for i in range(50):
    if pares==impares:
        pares=pares+1
    else:
        impares=impares+1

print(f"El número de números pares es de {pares}")
print(f"El número de números impares es de {impares}")
