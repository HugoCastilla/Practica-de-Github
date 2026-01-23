#ejercicio del DNI en el Sway

letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

intentos=[]
dnibien=[]
dnimal=[]
seguir="s"

while seguir=="s":
    dni = input("Introduce un DNI: ")
    if len(dni) !=8:
        print("Error: longitud incorrecta")
        intentos.append(0)
        dnimal.append(dni)
    elif not dni.isdigit():
        print("Error: no es numerico")
        intentos.append(1)
        dnimal.append(dni)
    else:
        numero=int(dni)
        resto=numero%23
        if resto<0 or resto>22:
            print("Error: resto no valido")
            intentos.append(2)
            dnimal.append(dni)
        else:
            letra=letras[resto]
            print("DNI correcto:", dni+"-"+letra)
            intentos.append(3)
            dnibien.append(dni)
    seguir=input("¿Quieres introducir otro DNI? (s/n): ")
opcion=""

while opcion !="5":
    print("MENÚ")
    print("1. Listar DNIs correctos")
    print("2. Listar DNIs incorrectos")
    print("3. Estadísticas")
    print("4. Lista de intentos")
    print("5. Salir")

    opcion=input("Elige una opción: ")
    if opcion=="1":
        dnibien.sort()
        print("DNIs correctos:")
        for d in dnibien:
            print(d)
    elif opcion=="2":
        dnimal.sort()
        print("DNIs incorrectos:")
        for d in dnimal:
            print(d)
    elif opcion=="3":
        total=len(intentos)
        correctos=intentos.count(3)
        errlong=intentos.count(0)
        errnum=intentos.count(1)
        ernesto=intentos.count(2)
        incorrectos=total - correctos
        if total>0:
            print("Total DNIs:", total)
            print("Correctos:", correctos)
            print("Incorrectos:", incorrectos)
            print("% Correctos:", (correctos*100)/total)
            print("% Incorrectos:", (incorrectos*100)/total)
            print("Errores de longitud:", errlong)
            print("Errores no numericos:", errnum)
            print("Errores de resto:", ernesto)
        else:
            print("No se han introducido DNIs")
    elif opcion=="4":
        print("Lista de intentos:", intentos)
    elif opcion=="5":
        print("Programa finalizado.")
    else:
        print("Opción incorrecta")