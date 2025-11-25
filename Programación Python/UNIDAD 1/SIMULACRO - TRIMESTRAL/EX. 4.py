valor = 100
if valor <= 50 or valor >= 150:
    print("El valor está fuera del rango permitido (50 < valor < 150).")
while True:
    numero = int(input("Introduce un número (negativo para salir): "))
    
    if numero < 0:
        print("Número negativo, saliendo del programa.")
        break
    
    if valor > 50 and valor < 150:
        if numero % 2 == 0:  # Par
            valor /= 2
        else:  # Impar
            valor += numero
            if numero % 3 == 0:  # Múltiplo de 3
                valor -= 5
    else:
        print("El valor está fuera del rango permitido (50 < valor < 150).")
    
    print(f"Valor actual: {valor}")