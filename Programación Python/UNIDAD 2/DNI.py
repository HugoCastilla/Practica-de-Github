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
