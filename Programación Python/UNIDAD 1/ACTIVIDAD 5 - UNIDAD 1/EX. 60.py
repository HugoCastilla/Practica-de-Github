#Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while

mul=int(input("Introduce un número: "))
multot=0
multigito=0
while multot<=(mul*9):
    multigito=multigito+1
    multot=mul*multigito
    print(f"{mul} x {multigito} = {multot}")