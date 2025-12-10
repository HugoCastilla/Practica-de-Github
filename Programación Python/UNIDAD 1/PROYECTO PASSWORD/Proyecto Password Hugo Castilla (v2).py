password=""
intentos=0
lower=0
upper=0
uncin=0
sesnuev=0
simb=0
sym="*_@&/#"
#mostramos por pantalla las indicaciones que el usuario ha de cumplir
print("Bienvenido al programa. Siga las indicaciones para introducir su contraseña:")
print("")
print("Su contraseña debe tener entre 8 o más carácteres.")
print("")
while intentos!=3:
    print("Su contraseña debe seguir estas características: ")
    print ("- 2 números mayores o iguales a 1 o menores o iguales a 5.")
    print ("- 2 letras minúscula.")
    print ("- Una letra mayúscula.")
    print ("- 2 de estos símbolos: *, _ , @, &, /, #.")
    print ("- Un número mayor o igual a 6 o menor o igual a 9.")

    #calculamos la longitud de la contraseña y comprobamos si es correcta

    password=str(input("Siguiendo las indicaciones, introduzca su contraseña: "))
    intentos=intentos+1

    if len(password)>=8:
        for i in range(len(password)):
            dig=password[i]
            dig=str(dig)
            if dig.isdigit():
                dig=int(dig)
                if dig>=1 or dig<=5:
                    uncin=uncin+1
                elif dig==0:
                    uncin=uncin
                else:
                    sesnuev=sesnuev+1
            elif dig.isalpha():
                if dig.isupper():
                    upper=upper+1
                else:
                    lower=lower+1
            else:
                if dig in sym:
                    simb=simb+1




        if intentos==1:
            print(f"Ya ha introducido {intentos} contraseña.")
        else:
            print(f"Ya ha introducido {intentos} contraseñas.")
    else:
        print("")
        print(f"Su contraseña '{password}' es demasiado corta.")
        if intentos==1:
            print(f"Ya ha introducido {intentos} contraseña.")
        else:
            print(f"Ya ha introducido {intentos} contraseñas.")