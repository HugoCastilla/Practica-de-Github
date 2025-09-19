#Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas.
segundos=float(input("Introduce una cantidad de segundos: "))

minutos=segundos/60
horas=minutos/60

print(f"{segundos} segundos equivalen a {minutos} minutos.")
print(f"{segundos} segundos equivalen a {horas} horas.")