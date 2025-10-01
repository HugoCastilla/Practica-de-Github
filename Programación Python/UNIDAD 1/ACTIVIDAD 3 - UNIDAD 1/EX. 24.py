#Corrige los errores del siguiente código y comprueba que se ejecuta correctamente

var1=float(input("Introduce el peso: "))
var2=float(input("Introduce la altura: "))
var_imc=var1/var2**2
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es: {var_imc}")
if var_imc>25:
 print("Hay sobrepeso")
else:
 print("Estás dentro de los parámetros normales")

#ERRORES CORREGIDOS:
 #print("Si pesas {1Var} kilos y mides {2var}, tu IMC es:", var_imc) --> print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es: {var_imc}")

 #if var_imc>25 --> if var_imc>25:

 #2var=(input("Introduce la altura: ")) --> var2=float(input("Introduce la altura: "))

 #var_imc==1var/2var**2 --> var_imc=var1/var2**2
