inicio=int(input("Ingrese un numero de inicio: "))
fin=int(input("Ingrese un numero de fin: "))
inc=int(input("Ingrese el incremento: "))

conc=""

for i in range(inicio, fin, inc):
    if i%4==0:
        conc=conc
    elif i%6==0:
        conc=conc+"*"+str(i)+"*"+","
    else:
        conc=conc+str(i)+","

print(conc[:-1])