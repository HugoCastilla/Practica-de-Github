#creamos la tabla de tipos de gasolina a escoger
print("*******GASOLINERA*******")
print("Orden | Nombre | Precio | Descuento")
print("1 | Sin Plomo 95 | 1.765 Euros | 0%")
print("2 | Sin Plomo 98 | 1.913 Euros | 10%")
print("3 | Gasóleo A | 1.746 Euros | 0%")
print("4 | Gasólero A+ | 1.839 Euros | 12%")
print("************************")

#pedimos al usuario el tipo de combustible y los litros
gas=input("Escoja un tipo de gasolina (1-4): ")
litros=float(input("Introduzca el número de litros a repostar: "))

#definimos las condiciones
if gas=="1":
    precio=1.765*litros
    desc=0
    preciodesc=round(precio*(1-desc), 2)
    print(f"El precio a pagar es {precio}, este combustible no cuenta con descuento.")
elif gas=="2":
    precio=1.913*litros
    desc=0.1
    preciodesc=round(precio*(1-desc), 2)
    print(f"El precio a pagar es {precio}, con el descuento se queda en {preciodesc}.")
elif gas=="3":
    precio=1.746*litros
    desc=0
    preciodesc=round(precio*(1-desc), 2)
    print(f"El precio a pagar es {precio}, este combustible no cuenta con descuento.")
elif gas=="4":
    precio=1.839*litros
    desc=0.12
    preciodesc=round(precio*(1-desc), 2)
    print(f"El precio a pagar es {precio}, con el descuento se queda en {preciodesc}.")
else:
    print("El combustibe escogido no existe.")