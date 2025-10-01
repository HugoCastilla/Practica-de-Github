#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

nota=float(input("Introduce la nota del alumno: "))

if nota>=5 and nota<=10:
    print(f"El alumno ha aprobado con un {nota} de media.")
elif nota<5 and nota>=0:
    print(f"El alumno ha suspendido con un {nota} de media.")
else:
    print("Esa nota no es válida.")
