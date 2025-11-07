#Imprima el siguiente patrón con el ciclo for:
#*
#**
#***
#****
#*****
#****
#***
#**
#*

patron="*"
marca=""
for i in range(9):
    print(patron)
    if marca=="":
        if patron=="*":
            patron="**"
        elif patron=="**":
            patron="***"
        elif patron=="***":
            patron="****"
        elif patron=="****":
            patron="*****"
            marca="@"
    else:
        if patron=="*****":
            patron="****"
        elif patron=="****":
            patron="***"
        elif patron=="***":
            patron="**"
        elif patron=="**":
            patron="*"
            marca=""