#ejercicio del DNI en el Sway

#definimos las letras en el orden establecido
letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
totcor=0
toterr=0
long=0
malnum=0
maletra=0
intentos=[]
dnibien=[]
dnimal=[]
seguir="s"
seseguir=""
opcion=""
#hacemos que el bucle se repita hasta que el usuario diga "n"
while seguir!="n":
    dni=input("Introduce un DNI: ")
    if len(dni)!=8:
        print("Error: longitud incorrecta")
        long=long+1
        toterr=toterr+1
        dnimal.append(dni)
    elif not dni.isdigit():
        print("Error: no es numerico")
        maletra=maletra+1
        toterr=toterr+1
        dnimal.append(dni)
    else:
        #calculamos la letra del dni dependiendo del residuo de la división
        numero=int(dni)
        resto=numero%23
        if resto<0 or resto>22:
            print("Error: resto no valido")
            malnum=malnum+1
            toterr=toterr+1
            dnimal.append(dni)
        else:
            letra=letras[resto]
            print("DNI correcto:", dni+"-"+letra)
            totcor=totcor+1
            dnibien.append(dni+"-"+letra)
    #ponemos lower para que si introduce la "n" o la "s" mayúscula cuente también
    seseguir=""
    while seseguir!="s" or "n":
        seseguir=input("¿Quieres introducir otro DNI? (s/n): ").lower()
        seguir=seseguir
        if seseguir!="s" or "n":
            print("Error.")

while opcion !="6":
    #mostramos las opciones posibles, uso prints vacios para dejar un poco de espacio en la salida y que quede mejor visualmente
    print("")
    print("MENÚ")
    print("1. Listar DNIs correctos")
    print("2. Listar DNIs incorrectos")
    print("3. Número total de errores")
    print("4. Número total de DNIs correctos")
    print("5. Porcentages")
    print("6. Salir")

    opcion=input("Elige una opción: ")
    print("")
    if opcion=="1":
        if totcor!=0:
            dnibien.sort()
            print("DNIs correctos:")
            print(dnibien)
        else:
            print("No se han introducido DNIs correctos")
    elif opcion=="2":
        if toterr!=0:
            dnimal.sort()
            print("DNIs incorrectos:")
            print(dnimal)
        else:
            print("No se han introducido DNIs incorrectos")
    elif opcion=="3":
        print("Número total de errores:", toterr)
    elif opcion=="4":
        print("Número total de DNIs correctos:", totcor)
    elif opcion=="5":
        total=toterr+totcor
        if total==0:
            print("No se han ingresado DNIs.")
        else:
            porcentaje=round((totcor/total)*100, 1)
            print("Porcentaje de DNIs correctos:",porcentaje)
            porcentmalje=round(100-porcentaje, 1)
            print("Porcentaje de DNIs incorrectos:",porcentmalje)
            porcentlong=round((long/total)*100, 1)
            print("Porcentaje de DNIs con longitud incorrecta:",porcentlong)
            porcenmalnum=round((malnum/total)*100,1 )
            print("Porcentaje de DNIs con error de dígitos:",porcenmalnum)
            porcenletra=round((maletra/total)*100, 1)
            print("Porcentaje de DNIs que no existen:",porcenletra)
    elif opcion=="6":
        print("Fin del programa.")
    else:
        print("Error. Esa opción no esta en la lista.")