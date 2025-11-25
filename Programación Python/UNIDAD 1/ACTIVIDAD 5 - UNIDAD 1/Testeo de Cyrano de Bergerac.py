#WHILE

i=1
while i<10:
    print("hola"+str(i))
    i+=1

#===============================================================================================================

edad=int(input("Introduce la edad: "))

while edad>100 or edad<0:
    print("Edad incorrecta")
    edad=int(input("Vuelve a introducir tu edad: "))
    if edad==999:
        break
print("Tu edad es correcta")