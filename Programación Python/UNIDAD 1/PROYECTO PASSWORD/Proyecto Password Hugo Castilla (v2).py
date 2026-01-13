password=""
intentos=0
lower=0
upper=0
uncin=0
sesnuev=0
simb=0
sym="*_@&/#"
correcto=0
incorrecto=0

#mostramos por pantalla las indicaciones que el usuario ha de cumplir
print("Bienvenido al programa. Siga las indicaciones para introducir su contraseña:")
print("")
while intentos!=3:
    print("Su contraseña debe seguir estas características: ")
    print("")
    print("- Su contraseña debe tener entre 8 o más carácteres.")
    print ("- 2 números mayores o iguales a 1 o menores o iguales a 5.")
    print ("- 2 letras minúscula.")
    print ("- Una letra mayúscula.")
    print ("- 2 de estos símbolos: *, _ , @, &, /, #.")
    print ("- Un número mayor o igual a 6 o menor o igual a 9.")

    #calculamos la longitud de la contraseña y comprobamos si es correcta
    print("")
    password=str(input("Siguiendo las indicaciones, introduzca su contraseña: "))
    print("")
    intentos=intentos+1

    if len(password)>=8:
        for i in range(len(password)):
            dig=password[i]
            dig=str(dig)
            if dig.isdigit():
                dig=int(dig)
                if dig>=1 and dig<=5:
                    uncin=uncin+1
                if dig==0:
                    uncin=uncin
                if dig>=6 and dig<=9:
                    sesnuev=sesnuev+1
            elif dig.isalpha():
                if dig.isupper():
                    upper=upper+1
                else:
                    lower=lower+1
            else:
                if dig in sym:
                    simb=simb+1
        
        if uncin<2:
            print("Error. Su contraseña no cuenta con suficientes números entre 1 y 5.")
        if sesnuev<1:
            print("Error. Su contraseña no cuenta con suficientes números entre el 6 y el 9.")
        if upper<1:
            print("Error. Su contraseña no cuenta con suficientes letras mayúsculas.")
        if lower<2:
            print("Error. Su contraseña no cuenta con suficientes letras minúsculas")
        if simb<2:
            print("Error. Su contraseña no cuenta con suficientes de estos símbolos: *, _ , @, &, /, #.")
        
        if uncin>=2 and sesnuev>=1 and upper>=1 and lower>=2 and simb>=2:
            print("Contraseña correcta.")
            print("")
            correcto=correcto+1
        else:
            incorrecto=incorrecto+1

        if intentos==1:
            print(f"Ya ha introducido {intentos} contraseña.")
            print("")
        else:
            print(f"Ya ha introducido {intentos} contraseñas.")
            print("")
    else:
        print("")
        print(f"Su contraseña '{password}' es demasiado corta.")
        print("")
        incorrecto=incorrecto+1

        if intentos==1:
            print(f"Ya ha introducido {intentos} contraseña.")
            print("")
        else:
            print(f"Ya ha introducido {intentos} contraseñas.")
            print("")

print(f"Ha introducido {correcto} contraseña/s correctas y {incorrecto} contraseña/s incorrectas.")



#INTENTOS DE CONTRASEÑAS:

# - 623MMmm** - Correcta

# - 623Mmm** - Correcta

# - "" - Incorrecta (Menos de 8 caracteres)

# - 99999999999999999iLoP@&13 - Correcta

# - 10Kjp&88 - Incorrecta (Menos de dos números entre 1 y 5)(Menos de 2 símbolos)

# - 1234567890qwertyuiopasdfghjklñçzxcvbnm!@#$%&/() - Correcta

# - 23tT_8 - Incorrecta (Menos de 8 caracteres)

# - Castilla_La_Mancha7/34 - Correcta

# - x2ge7cv4c27r$%&% - Incorrecta (Menos de 2 mayúsculas)(Menos de dos símbolos)

# - ccacahuUetes91873 - Incorrecta (Menos de 2 símbolos)
