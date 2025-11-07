#A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10

notas=int(input("Introduce el número de notas que deseas introducir: "))

for i in range(notas):
    nota=float(input("Introduce una nota: "))
    if nota<0:
        print("Esa nota no es válida")
    elif nota>10:
        print("Esa nota no es válida")
    else:
        if nota<5:
            print(f"Has suspendido")
        else:
            print(f"Estás aprobado")
