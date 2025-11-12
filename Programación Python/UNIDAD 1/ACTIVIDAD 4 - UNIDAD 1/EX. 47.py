#Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida

intervalo1=int(input("Introduce el primer intervalo: "))
intervalo2=int(input("Introduce el segundo intervalo: "))

for i in range(intervalo1, intervalo2+1):
    if intervalo1<intervalo2:
        print(i, end="-" if i < intervalo2 else "")
    elif intervalo1>intervalo2:
        print(i, end="-" if i > intervalo1 else "")


#WIP