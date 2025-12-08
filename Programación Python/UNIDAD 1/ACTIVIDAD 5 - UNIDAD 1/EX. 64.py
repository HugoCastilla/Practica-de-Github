#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas: 
#a) total de pares 
#b) total de impares 
#c) total de números positivos 
#d) total de números negativos 
#e) total de ceros 
#f) total de la suma de todos los números introducidos 
par=0
imp=0
pos=0
neg=0
cero=0
sum=0
num=0

while num!=-99:
    num=int(input("Introduzca un número: "))
    if num==-99:
        break
    if num%2==0:
        par=par+1
    else:
        imp=imp+1
    if num<0:
        pos=pos+1
    elif num>0:
        neg=neg+1
    else:
        cero=cero+1
    sum=sum+num
print("Número de pares:", par)
print("Número de impares:", imp)
print("Número de positivos:", pos)
print("Número de negativos:", neg)
print("Número de ceros:", cero)
print("Suma total:", sum)
