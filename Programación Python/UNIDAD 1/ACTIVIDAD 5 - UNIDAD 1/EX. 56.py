#Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.

ped=0
pedido="S"
superdido=0

print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")

while pedido=="S":
    ped=ped+1
    boc=int(input("Escoja su bocadillo (1-3): "))
    if boc==1:
        preboc=9
    elif boc==2:
        preboc=4.5
    elif boc==3:
        preboc=2.5
    else:
        print("Ese bocadillo no existe.")

    acom=int(input("Escoja su acompañamiento (1-3): "))
    if acom==1:
        preacom=1.5
    elif acom==2:
        preacom=1.75
    elif acom==3:
        preacom=2
    else:
        print("Ese acompañamiento no existe.")

    beb=int(input("Escoja su bebida (1-3): "))
    if beb==1:
        prebeb=2
    elif beb==2:
        prebeb=1.5
    elif beb==3:
        prebeb=1
    else:
        print("Esa bebida no existe.")

    tot=preboc+preacom+prebeb
    superdido=superdido+tot

    if superdido>=20 and superdido<=30:
        desc=0.9
        des=10
    elif superdido>30:
        desc=0.85
        des=15
    else:
        desc=1
        des=0
        
    print(f"El total a pagar sin IVA ni descuentos es de {superdido}")
    pedido=input("Quiere realizar otro pedido (S/N): ")

print(f"Este es su pedido número {ped}.")
print(f"El total a pagar a pagar es de {superdido} euros.")
superdido=superdido*1.1
print(f"El precio con IVA aplicado es de {superdido} euros.")
superdesc=superdido*desc
print(f"El precio total con un descuento del {des}% es de {superdesc}")
print("Que tenga un buen día.")