password=""
intentos=0

#mostramos por pantalla las indicaciones que el usuario ha de cumplir
print("Bienvenido al programa. Siga las indicaciones para introducir su contraseña:")
print("")
print("Su contraseña debe tener entre 8 o más carácteres.")
print("")
print("Su contraseña debe seguir estas características: ")
print ("- Un número mayor o igual a 1 o menor o igual a 5.")
print ("- 2 letras minúscula.")
print ("- Una letra mayúscula.")
print ("- Uno de estos símbolos: *, _ , @.")
print ("- Un número mayor o igual a 6 o menor o igual a 9.")
print ("- Uno de estos símbolos: &, /, #.")
print ("- Un número menor o igual a 5 (No puede ser negativo).")

#calculamos la longitud de la contraseña y comprobamos si es correcta

password=str(input("Siguiendo las indicaciones, introduzca su contraseña: "))
intentos=intentos+1

if len(password)>=8:
    print("Vale.")
else:
    print(f"Su contraseña '{password}' es demasiado corta.")
    if intentos==1:
        print(f"Ya ha introducido {intentos} contraseña.")
    else:
        print(f"Ya ha introducido {intentos} contraseñas.")