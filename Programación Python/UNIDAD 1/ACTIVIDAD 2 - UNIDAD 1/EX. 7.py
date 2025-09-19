#Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

var1=float(input("Introduce el primer operando: "))
var2=float(input("Introduce el segundo operando: "))

#SUMA
suma=var1+var2
print("La suma de ambos valores es", suma)
#RESTA
resta=var1-var2
print("La resta de ambos valores es", resta)
#MULTIPLICACIÓN
producto=var1*var2
print("El producto de ambos valores es", producto)
#DIVISÍON
división=var1/var2
print(f"La división de ambos valores es {división:.2f}")
#EXPONENTE
exponente=var1**var2
print("El valor del exponente de ambos valores es", exponente)
#DIVISIÓN ENTERA
diventera=round(var1/var2,0)
print("La división entera de ambos valores es", diventera)
#MÓDULO
modulo=var1%var2
print("El módulo de ambos valores es", modulo)