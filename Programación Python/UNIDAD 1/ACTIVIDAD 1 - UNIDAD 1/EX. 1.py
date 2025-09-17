print("Buenos días, bienvenido a 'Calculadora', por Hugo Castilla")
var1=input("¿Qué tipo de cálculo quieres hacer? (suma, resta)")
if (var1=="suma"):
    var2=int(input("Introduzca un número: "))
    var3=int(input("Introduzca un segundo número: "))
    total = var2+var3
    print("La suma de ambos números es", total)
if (var1=="resta"):
    var2=int(input("Introduzca un número: "))
    var3=int(input("Introduzca un segundo número: "))
    total = var2-var3
    print("La resta de ambos números es", total)