 #Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas

frase=("A quién madruga Dios le ayuda")

minusculas=frase.lower()
if "dios" in minusculas:
    print("La palabra 'dios' está en la frase y está en el índice", minusculas.index("dios"))
else:
    print("La palabra 'dios' no está en la frase")
if "madruga" in minusculas:
    print("La palabra 'madruga' está en la frase y está en el índice", minusculas.index("madruga"))
else:
    print("La palabra 'madruga' no está en la frase")
if "Dios" in frase:
    print("La palabra 'Dios' está en la frase y está en el índice", frase.index("Dios"))
else:
    print("La palabra 'Dios' no está en la frase")
