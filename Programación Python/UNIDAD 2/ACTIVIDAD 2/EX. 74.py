#A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas

lista1 =["casa", "mesa", "sal", "sol", "agua"]
lista2 =["casa", "luz", "tres", "tren", "sol", "pan"]
rep=[]
norep=[]
for x in lista1:
    if x in lista2:
        rep.append(x)
    else:
        norep.append(x)

for x in lista2:
    if x in lista1 and x not in rep:
        rep.append(x)
    else:
        norep.append(x)
print("Las palabras que se repiten son:", rep)
print("Las palabras que no se repiten son:", norep)