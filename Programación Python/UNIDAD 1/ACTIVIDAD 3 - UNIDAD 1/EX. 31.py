#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

frase=("A quién madruga Dios le ayuda")

if "Dios" in frase:
    print("La palabra 'Dios' está en la frase y está en el índice", frase.index("Dios"))
else:
    print("La palabra 'Dios' no está en la frase")
if "dios" in frase:
    print("La palabra 'dios' está en la frase y está en el índice", frase.index("dios"))
else:
    print("La palabra 'dios' no está en la frase")
if "madruga" in frase:
    print("La palabra 'madruga' está en la frase y está en el índice", frase.index("madruga"))
else:
    print("La palabra 'madruga' no está en la frase")
