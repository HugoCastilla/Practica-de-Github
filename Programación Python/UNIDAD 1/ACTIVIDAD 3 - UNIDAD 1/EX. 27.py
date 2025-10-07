#Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla

txt=input("Introduce una letra o número: ")
if txt.isupper()==True:
    print("La letra es mayúscula")
elif txt.islower()==True:
    print("La letra es minúscula")
elif txt.isdigit()==True:
    print("Es un número")
else:
    print("El carácter no es una letra ni un número")