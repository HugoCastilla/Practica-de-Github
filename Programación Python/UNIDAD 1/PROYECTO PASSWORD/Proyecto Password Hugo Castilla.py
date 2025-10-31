#definimos las variables que indican en que caràcter se encuentra el error
err1=""
err2=""
err3=""
err4=""
err5=""
err6=""
err7=""
err8=""

#mostramos por pantalla las indicaciones que el usuario ha de cumplir
print("Bienvenido al programa. Siga las indicaciones para introducir su contraseña:")
print("")
print("Su contraseña debe tener entre 6 y 8 carácteres.")
print ("1º carácter: Número mayor o igual a 1 o menor o igual a 5.")
print ("2º carácter: Letra minúscula.")
print ("3º carácter: Letra mayúscula.")
print ("4º carácter: Uno de estos símbolos: *, _ , @.")
print ("5º carácter: Letra minúscula.")
print ("6º carácter: Número mayor o igual a 6 o menor o igual a 9.")
print ("7º carácter: Uno de estos símbolos: &, /, #.")
print ("8º carácter: Un número menor o igual a 5 (No puede ser negativo).")

#calculamos la longitud de la contraseña y comprobamos si es correcta
password=str(input("Siguiendo las indicaciones, introduzca su contraseña: "))

if len(password)>=6 and 8>=len(password):
    if password[0]<="5" and password[0]>="1":
        err1=("")
    else:
        err1="Error en el 1º caràcter."
    if password[1].islower():
        err2=("")
    else:
        err2="Error en el 2º caràcter."
    if password[2].isupper():
        err3=("")
    else:
        err3="Error en el 3º caràcter."
    if password[3]=="*" or password[3]=="_" or password[3]=="@":
        err4=("")
    else:
        err4="Error en el 4º caràcter."
    if password[4].islower():
        err5=("")
    else:
        err5="Error en el 5º caràcter."
    if password[5]>="6" and password[5]<="9":
        err6=("")
    else:
        err6="Error en el 6º caràcter."
    if len(password)>6:
        if password[6]=="&" or password[6]=="/" or password[6]=="#":
            err7=("")
        else:
            err7="Error en el 7º caràcter."
    if len(password)>7:
        if password[7]>="0" and password[7]<="5":
            err8=("")
        else:
            err8="Error en el 8º caràcter."
    #mostramos los errores que tiene la contraseña
    if err1=="" and err2=="" and err3=="" and err4=="" and err5=="" and err6=="" and err7=="" and err8=="":
        print("Contraseña correcta. Acceso garantizado al programa.")
    else:
        print(f"{err1} {err2} {err3} {err4} {err5} {err6} {err7} {err8}")
else:
    if len(password)>8:
        carac=len(password)
        print(f"Su contraseña de {carac} carácteres excede los carácteres requeridos.")
    else:
        carac=len(password)
        print(f"Su contraseña de {carac} carácteres no alcanza los carácteres requeridos.")
