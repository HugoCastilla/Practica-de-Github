#Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
numero=input("Introduce un número: ")
partes=numero.split(".")
if len(partes)==2 and partes[0].isdigit() and partes[1].isdigit():
    print(f"El número {numero} es decimal.")
else:
    print(f"El número {numero} no es decimal.")
