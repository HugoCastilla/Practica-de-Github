print("1 | Tarifa Nocturna | 0.158 euros | 5%")
print("2 | Tarifa Plana | 0.192 euros | 0%")
print("3 | Tarifa Solar | 0.143 euros | 8%")
print("4 | Tarifa Ecológica | 0.170 euros | 10%")

tarifa=input("Escoja una opcion de tarifa (1-4): ")
kwh=float(input("Introduzca los kWh: "))

if tarifa=="1":
    precio=round(kwh*0.158, 2)
    desc=round(precio*0.05, 2)
    total=round(precio-desc, 2)
    print("El total a pagar es de", precio, "euros.")
    print(" Con el descuento aplicado queda en", total, "euros.")

elif tarifa=="2":
    precio=round(kwh*0.192, 2)
    desc=round(precio*0, 2)
    total=round(precio-desc, 2)
    print("El total a pagar es de", precio, "euros.")
    print(" Con el descuento aplicado queda en", total, "euros.")

elif tarifa=="3":
    precio=round(kwh*0.143, 2)
    desc=round(precio*0.08, 2)
    total=round(precio-desc, 2)
    print("El total a pagar es de", precio, "euros.")
    print(" Con el descuento aplicado queda en", total, "euros.")

elif tarifa=="4":
    precio=round(kwh*0.170, 2)
    desc=round(precio*0.10, 2)
    total=round(precio-desc, 2)
    print("El total a pagar es de", precio, "euros.")
    print(" Con el descuento aplicado queda en", total, "euros.")

else:
    print("Error, esa tarifa no existe")

