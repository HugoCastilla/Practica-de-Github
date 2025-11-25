# Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

notas=int(input("Introduce el número de notas que deseas introducir: "))

for i in range(notas):
    nota=float(input("Introduce una nota: "))
    if nota<5:
        print(f"Has suspendido")
    else:
        print(f"Estás aprobado")
