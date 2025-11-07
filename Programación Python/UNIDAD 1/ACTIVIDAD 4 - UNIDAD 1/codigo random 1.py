# Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

notas=int(input("Introduce el número de notas que deseas introducir: "))
sumanota=0
media=0

for i in range(notas):
    nota=float(input("Introuduce una nota: "))
    sumanota=sumanota+nota

media=round(sumanota/notas, 2)
if media<5:
    print(f"Estás suspendido con una media de {media}")
else:
    print(f"Estás aprobado con una media de {media}")