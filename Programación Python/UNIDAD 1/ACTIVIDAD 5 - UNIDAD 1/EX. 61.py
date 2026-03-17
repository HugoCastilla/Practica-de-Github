#A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40

mul=int(input("Introduce un número: "))
multot=0
multigito=0

while multot<=mul*9 and multot<40:
    multigito=multigito+1
    multot=mul*multigito
    print(f"{mul} x {multigito} = {multot}")