# Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

txt=input("Ingrese un carácter: ")
if txt.islower()==True:
    print("El carácter es minúscula")
elif txt.isupper()==True:
    print("El carácter es mayúscula")
elif txt.isnumeric()==True:
    print("El carácter es un número")
elif not txt.isalnum()==True:
    print("El carácter es un símbolo")