#Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
#se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 

import time
import random

def simular_dado_durante(segundos=3):
    # Contadores para cada cara del dado (índice 0 no se usa)
    conteo = [0] * 7  # posiciones 1 a 6

    inicio = time.time()
    tiradas = 0

    # Lanzar el dado hasta que pasen 'segundos'
    while time.time() - inicio < segundos:
        cara = random.randint(1, 6)  # número aleatorio entre 1 y 6
        conteo[cara] += 1
        tiradas += 1

    # Mostrar resultados
    print(f"\nResultados después de {segundos} segundos ({tiradas} tiradas):")
    for cara in range(1, 7):
        print(f"Cara {cara}: {conteo[cara]} veces")

if __name__ == "__main__":
    try:
        simular_dado_durante(3)  # puedes cambiar el tiempo aquí
    except KeyboardInterrupt:
        print("\nSimulación interrumpida por el usuario.")
