#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

nota=float(input("Introduce la nota del alumno: "))

if nota<5:
    if nota>=0:
        print(f"El alumno ha suspendido con un {nota} de media.")
elif nota>=5:
    if nota<6.5:
        print(f"El alumno ha obtenido un satisfactorio con un {nota} de media.")
elif nota>=6.5:
    if nota<8.5:
        print(f"El alumno ha obtenido un notable con un {nota} de media.")
elif nota>=8.5:
    if nota<=10:
        print(f"El alumno ha obtenido un excelente con un {nota} de media.")
else:
    print("Esa nota no es válida.")