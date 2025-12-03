#Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

min=int(input("Introduce un número: "))
max=int(input("Introduce otro número: "))
imp=""
par=""

if min<=max:
    for i in range(min, max+1):
        if i%2==0:
            par=par+str(i)+"-"
        else:
            imp=imp+str(i)+"-"
else:
    for i in range(max, min+1):
        if i%2==0:
            par=par+str(i)+"-"
        else:
            imp=imp+str(i)+"-"
        
print(f"Los números pares son: {par}"[:-1])
print(f"Los números impares son: {imp}"[:-1])