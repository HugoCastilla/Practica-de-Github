var1=input("Introduce las contraseñas: ")
lista=var1.split("-")
conseguras=[]
coninseguras=[]
coninvalidas=[]
larga=""

for x in lista:
    nums=0
    letras=0
    caracteres=0
    for y in x:
        if y.isdigit():
            nums+=1
        elif y.isalpha():
            letras+=1
        else:
            caracteres+=1
    if caracteres>0:
        coninvalidas.append(x)
    else:
        if len(x)>=8 and x.isalnum():
            conseguras.append(x)
        else:
            coninseguras.append(x)
        if len(x)>len(larga):
            larga=x
print("Contraseñas seguras: ",conseguras)
print("Contraseñas inseguras: ",coninseguras)
print("Contraseñas inválidas: ",coninvalidas)
print("Contraseña más larga: ",larga)