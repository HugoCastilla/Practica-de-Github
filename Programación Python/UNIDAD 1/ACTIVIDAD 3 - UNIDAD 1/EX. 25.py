#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

nota=float(input("Introduce la nota del alumno: "))

if nota<5 and nota>=0:
    print(f"El alumno ha suspendido con un {nota} de media.")
elif nota>=5 and nota<6.5:
    print(f"El alumno ha obtenido un satisfactorio con un {nota} de media.")
elif nota>=6.5 and nota<8.5:
    print(f"El alumno ha obtenido un notable con un {nota} de media.")
elif nota>=8.5 and nota<=10:
    print(f"El alumno ha obtenido un excelente con un {nota} de media.")
else:
    print("Esa nota no es válida.")