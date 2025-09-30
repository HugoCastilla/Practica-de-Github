print("Menú:")
print("1. Hamburguesa")
print("2. Pizza")
print("3. Lentejas")
print("4. Bocadillo de jamón")

plato=float(input("Elige un plato (1-4): "))
plato=round(plato)

if plato==1:
    print("Marchando una hamburguesa")
if plato==2:
    print("Marchando una pizza")
if plato==3:
    print("Marchando unas lentejas")
if plato==4:
    print("Marchando un bocadillo de jamón")
if plato>4 or plato<1:
    print("Ese plato no está en el menú")