#definimos las variables que indican en que caràcter se encuentra el error
err1=0
err2=0
err3=0
err4=0
err5=0
err6=0
err7=0
err8=0

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
        print("bien")
    else:
        err1=1
        print("mal")
    if password[1].islower():
        print("bien")
    else:
        err2=1
        print("mal")
    if password[2].isupper():
        print("bien")
    else:
        err3=1
        print("mal")
    if password[3]=="*" or password[3]=="_" or password[3]=="@":
        print("bien")
    else:
        err4=1
        print("mal")
    if password[4].islower():
        print("bien")
    else:
        err5=1
        print("mal")
    if password[5]>="6" and password[5]<="9":
        print("bien")
    else:
        err6=1
        print("mal")
    if password[6]=="&" or password[6]=="/" or password[6]=="#":
        print("bien")
    else:
        err7=1
        print("mal")
    if password[7]>="0" and password[5]<="5":
        print("bien")
    else:
        err8=1
        print("mal")

else:
    if len(password)>8:
        print("Su contraseña excede el número de carácteres solicitados.")
    else:
        print("Su contraseña no alcanza el número de carácteres solicitados.")