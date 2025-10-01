# A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10

num1=int(input("Introduce un número entre el 0 y el 10: "))
num2=int(input("Introduce otro número entre el 0 y el 10: "))

if num1<0 or num1>10 or num2<0 or num2>10:
    print("Uno de los valores no se encuentra en el rango de números permitido.")
elif num1>num2:
    print(f"El número {num1} es mayor que el número {num2}.")
elif num1<num2:
    print(f"El número {num1} es menor que el número {num2}.")
else:
    print("Los dos números son iguales.")