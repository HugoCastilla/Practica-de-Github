#definimos las variables
password="a82yabei29"
total=0
voc="aeiouAEIOU"
vocals=0

#hacemos la suma de todos los números
for i in password:
    if i.isnumeric():
        total=total+int(i)

#miramos cuantas vocales hay
for j in password:
    if j in voc:
        vocals=vocals+1

#mostramos por pantalla los resultados
print(total)
print(vocals)