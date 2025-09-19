#Programa que pida un número de horas y muestre por pantalla los minutos y segundos.
horas=int(input("Introduce un número de horas: "))

minutos=horas*60
segundos=minutos*60

print(f"En {horas} hora/s hay {minutos} minutos.")
print(f"En {horas} hora/s hay {segundos} segundos.")