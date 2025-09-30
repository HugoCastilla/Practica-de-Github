#>,<,=,>=,<=,!=

num1=int(input("Introduce un número: "))
num2=int(input("Introduce otro número: "))

# "!=" quiere decir "distinto de".
if num1!=num2:
    print("Los números son distintos")

# ">" quiere decir "mayor que".
if num1>num2:
    print(f"{num1} es mayor que {num2}")

# "<" quiere decir "menor que".
if num1<num2:
    print(f"{num1} es menor que {num2}")

# "==" quiere decir "igual a".
# Si no se ponen dos iguales, el programa le asigna el valor de una variable a la otra.
if num1==num2:
    print("Los números son iguales")

