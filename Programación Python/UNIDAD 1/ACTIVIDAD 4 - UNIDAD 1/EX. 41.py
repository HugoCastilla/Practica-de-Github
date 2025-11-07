#Imprime el siguiente patrón utilizando for:
#54321
#4321
#321
#21
#1

patron=54321

for i in range(5):
    print(patron)
    if patron>9999:
        patron=patron-50000
    elif patron>999:
        patron=patron-4000
    elif patron>99:
        patron=patron-300
    elif patron>9:
        patron=patron-20
    