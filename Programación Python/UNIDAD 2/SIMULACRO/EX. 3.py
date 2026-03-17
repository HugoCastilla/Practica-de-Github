cosas=input("Introduzca los datos necesarios: ")
listaprecio=[]
listaproducto=[]
listastock=[]
total=0
for i in cosas.split("-"):
    listaproducto.append(i.split(":")[0])
    listaprecio.append(i.split(":")[1])
    listastock.append(i.split(":")[2])

listaprecio=[int(i) for i in listaprecio]
listastock=[int(i) for i in listastock]

total=sum(listastock)*sum(listaprecio)
mascaro=listaprecio.index(max(listaprecio))
igualacero=listastock.index(0)

print("El total de la compra es: ",total)
print("El producto más caro es: ",listaproducto[mascaro])
print("El producto con stock 0 es: ",listaproducto[igualacero])

listaproducto.remove(listaproducto[igualacero])

print("Los productos restantes son: ",listaproducto)