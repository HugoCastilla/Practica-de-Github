#Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.

num=int(input("Introduce el número de números que deseas introducir: "))
negativos=0
positivos=0
ceros=0

for i in range(num):
    nom=float(input("Introduce un número: "))
    if nom<0:
        negativos=negativos+1
    elif nom>0:
        positivos=positivos+1
    else:
        ceros=ceros+1

print(f"El número de números positivos es de {positivos}")
print(f"El número de números negativos es de {negativos}")
print(f"El número de ceros es {ceros}")