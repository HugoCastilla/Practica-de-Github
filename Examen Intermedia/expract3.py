cif=int(input("Introduce un número de cifras: "))
num=int(input(f"Introduce un número de {cif} cifras: "))
prod=1
par=0

if cif==len(str(num)):
    for i in range(cif):
        prod=prod*int(str(num)[i])
        if int(str(num)[i])%2==0:
            par=par+1
    print("El producto de las cifras es:",prod)
    print("La cantidad de cifras pares es:",par)
else:
    print("Longitud incorrecta")
