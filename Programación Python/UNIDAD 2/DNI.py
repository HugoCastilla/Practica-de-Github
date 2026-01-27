#ejercicio del DNI en el Sway

#definimos las letras en el orden establecido
letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

intentos=[]
dnibien=[]
dnimal=[]
seguir="s"
opcion=""
#hacemos que el bucle se repita hasta que el usuario diga "n"
while seguir!="n":
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
        #calculamos la letra del dni dependiendo del residuo de la división
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
    #ponemos lower para que si introduce la "n" mayúscula cuente también
    seguir=input("¿Quieres introducir otro DNI? (s/n): ").lower()

while opcion !="6":
    #mostramos las opciones posibles
    print("MENÚ")
    print("1. Listar DNIs correctos")
    print("2. Listar DNIs incorrectos")
    print("3. Número total de errores")
    print("4. Número total de DNIs correctos")
    print("5. Porcentage de DNI correcto")
    print("6. Salir")

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
        toterr=intentos.count(0)+intentos.count(1)+intentos.count(2)
        print("Número total de errores:", toterr)
    elif opcion=="4":
        totcor=intentos.count(3)
        print("Número total de DNIs correctos:", totcor)
    elif opcion=="5":
        total=intentos.count(0)+intentos.count(1)+intentos.count(2)+intentos.count(3)
        if total==0:
            print("No se han ingresado DNIs.")
        else:
            porcentaje=(totcor/total)*100
            print("Porcentaje de DNIs correctos:",porcentaje)
    elif opcion=="6":
        print("Fin del programa.")
    else:
        print("Error. Esa opción no esta en la lista.")