import random

dinero=20
seguir="s"
suma=0
sumacrupier=0
pedir=""
numcar=0
while seguir=="s":
    print("Cartas iniciales:")
    numcar=random.randint(1,14)
    palo=random.randint(1,4)
    if numcar==1 and palo==1:
        carta1="As de corazones"
    if numcar==1 and palo==2:
        carta1="As de picas"
    if numcar==1 and palo==3:
        carta1="As de tréboles"
    if numcar==1 and palo==4:
        carta1="As de diamantes"
    if numcar==2 and palo==1:
        carta1="1 de corazones"
    if numcar==2 and palo==2:
        carta1="1 de picas"
    if numcar==2 and palo==3:
        carta1="1 de tréboles"
    if numcar==2 and palo==4:
        carta1="1 de diamantes"
    if numcar==3 and palo==1:
        carta1="2 de corazones"
    if numcar==3 and palo==2:
        carta1="2 de picas"
    if numcar==3 and palo==3:
        carta1="2 de tréboles"
    if numcar==3 and palo==4:
        carta1="2 de diamantes"
    if numcar==4 and palo==1:
        carta1="3 de corazones"
    if numcar==4 and palo==2:
        carta1="3 de picas"
    if numcar==4 and palo==3:
        carta1="3 de tréboles"
    if numcar==4 and palo==4:
        carta1="3 de diamantes"
    if numcar==5 and palo==1:
        carta1="4 de corazones"
    if numcar==5 and palo==2:
        carta1="4 de picas"
    if numcar==5 and palo==3:
        carta1="4 de tréboles"
    if numcar==5 and palo==4:
        carta1="4 de diamantes"
    if numcar==6 and palo==1:
        carta1="5 de corazones"
    if numcar==6 and palo==2:
        carta1="5 de picas"
    if numcar==6 and palo==3:
        carta1="5 de tréboles"
    if numcar==6 and palo==4:
        carta1="5 de diamantes"
    if numcar==7 and palo==1:
        carta1="6 de corazones"
    if numcar==7 and palo==2:
        carta1="6 de picas"
    if numcar==7 and palo==3:
        carta1="6 de tréboles"
    if numcar==7 and palo==4:
        carta1="6 de diamantes"
    if numcar==8 and palo==1:
        carta1="7 de corazones"
    if numcar==8 and palo==2:
        carta1="7 de picas"
    if numcar==8 and palo==3:
        carta1="7 de tréboles"
    if numcar==8 and palo==4:
        carta1="7 de diamantes"
    if numcar==9 and palo==1:
        carta1="8 de corazones"
    if numcar==9 and palo==2:
        carta1="8 de picas"
    if numcar==9 and palo==3:
        carta1="8 de tréboles"
    if numcar==9 and palo==4:
        carta1="8 de diamantes"
    if numcar==10 and palo==1:
        carta1="9 de corazones"
    if numcar==10 and palo==2:
        carta1="9 de picas"
    if numcar==10 and palo==3:
        carta1="9 de tréboles"
    if numcar==10 and palo==4:
        carta1="9 de diamantes"
    if numcar==11 and palo==1:
        carta1="10 de corazones"
    if numcar==11 and palo==2:
        carta1="10 de picas"
    if numcar==11 and palo==3:
        carta1="10 de tréboles"
    if numcar==11 and palo==4:
        carta1="10 de diamantes"
    if numcar==12 and palo==1:
        carta1="Q de corazones"
    if numcar==12 and palo==2:
        carta1="Q de picas"
    if numcar==12 and palo==3:
        carta1="Q de tréboles"
    if numcar==12 and palo==4:
        carta1="Q de diamantes"
    if numcar==13 and palo==1:
        carta1="J de corazones"
    if numcar==13 and palo==2:
        carta1="J de picas"
    if numcar==13 and palo==3:
        carta1="J de tréboles"
    if numcar==13 and palo==4:
        carta1="J de diamantes"
    if numcar==14 and palo==1:
        carta1="K de corazones"
    if numcar==14 and palo==2:
        carta1="K de picas"
    if numcar==14 and palo==3:
        carta1="K de tréboles"
    if numcar==14 and palo==4:
        carta1="K de diamantes"
    numcar=random.randint(1,14)
    palo=random.randint(1,4)
    if numcar==1 and palo==1:
        carta2="As de corazones"
    if numcar==1 and palo==2:
        carta2="As de picas"
    if numcar==1 and palo==3:
        carta2="As de tréboles"
    if numcar==1 and palo==4:
        carta2="As de diamantes"
    if numcar==2 and palo==1:
        carta2="1 de corazones"
    if numcar==2 and palo==2:
        carta2="1 de picas"
    if numcar==2 and palo==3:
        carta2="1 de tréboles"
    if numcar==2 and palo==4:
        carta2="1 de diamantes"
    if numcar==3 and palo==1:
        carta2="2 de corazones"
    if numcar==3 and palo==2:
        carta2="2 de picas"
    if numcar==3 and palo==3:
        carta2="2 de tréboles"
    if numcar==3 and palo==4:
        carta2="2 de diamantes"
    if numcar==4 and palo==1:
        carta2="3 de corazones"
    if numcar==4 and palo==2:
        carta2="3 de picas"
    if numcar==4 and palo==3:
        carta2="3 de tréboles"
    if numcar==4 and palo==4:
        carta2="3 de diamantes"
    if numcar==5 and palo==1:
        carta2="4 de corazones"
    if numcar==5 and palo==2:
        carta2="4 de picas"
    if numcar==5 and palo==3:
        carta2="4 de tréboles"
    if numcar==5 and palo==4:
        carta2="4 de diamantes"
    if numcar==6 and palo==1:
        carta2="5 de corazones"
    if numcar==6 and palo==2:
        carta2="5 de picas"
    if numcar==6 and palo==3:
        carta2="5 de tréboles"
    if numcar==6 and palo==4:
        carta2="5 de diamantes"
    if numcar==7 and palo==1:
        carta2="6 de corazones"
    if numcar==7 and palo==2:
        carta2="6 de picas"
    if numcar==7 and palo==3:
        carta2="6 de tréboles"
    if numcar==7 and palo==4:
        carta2="6 de diamantes"
    if numcar==8 and palo==1:
        carta2="7 de corazones"
    if numcar==8 and palo==2:
        carta2="7 de picas"
    if numcar==8 and palo==3:
        carta2="7 de tréboles"
    if numcar==8 and palo==4:
        carta2="7 de diamantes"
    if numcar==9 and palo==1:
        carta2="8 de corazones"
    if numcar==9 and palo==2:
        carta2="8 de picas"
    if numcar==9 and palo==3:
        carta2="8 de tréboles"
    if numcar==9 and palo==4:
        carta2="8 de diamantes"
    if numcar==10 and palo==1:
        carta2="9 de corazones"
    if numcar==10 and palo==2:
        carta2="9 de picas"
    if numcar==10 and palo==3:
        carta2="9 de tréboles"
    if numcar==10 and palo==4:
        carta2="9 de diamantes"
    if numcar==11 and palo==1:
        carta2="10 de corazones"
    if numcar==11 and palo==2:
        carta2="10 de picas"
    if numcar==11 and palo==3:
        carta2="10 de tréboles"
    if numcar==11 and palo==4:
        carta2="10 de diamantes"
    if numcar==12 and palo==1:
        carta2="Q de corazones"
    if numcar==12 and palo==2:
        carta2="Q de picas"
    if numcar==12 and palo==3:
        carta2="Q de tréboles"
    if numcar==12 and palo==4:
        carta2="Q de diamantes"
    if numcar==13 and palo==1:
        carta2="J de corazones"
    if numcar==13 and palo==2:
        carta2="J de picas"
    if numcar==13 and palo==3:
        carta2="J de tréboles"
    if numcar==13 and palo==4:
        carta2="J de diamantes"
    if numcar==14 and palo==1:
        carta2="K de corazones"
    if numcar==14 and palo==2:
        carta2="K de picas"
    if numcar==14 and palo==3:
        carta2="K de tréboles"
    if numcar==14 and palo==4:
        carta2="K de diamantes"
    print(carta1)
    print(carta2)
    if "As" in carta1:
        if suma>10:
            valor1=1
        else:
            valor1=11
    if "2" in carta1:
        valor1=2
    if "3" in carta1:
        valor1=3
    if "4" in carta1:
        valor1=4
    if "5" in carta1:
        valor1=5
    if "6" in carta1:
        valor1=6
    if "7" in carta1:
        valor1=7
    if "8" in carta1:
        valor1=8
    if "9" in carta1:
        valor1=9
    if "10" in carta1:
        valor1=10
    if "J" in carta1:
        valor1=10
    if "Q" in carta1:
        valor1=10
    if "K" in carta1:
        valor1=10


    if "As" in carta2:
        if suma>10:
            valor2=1
        else:
            valor2=11
    if "2" in carta2:
        valor2=2
    if "3" in carta2:
        valor2=3
    if "4" in carta2:
        valor2=4
    if "5" in carta2:
        valor2=5
    if "6" in carta2:
        valor2=6
    if "7" in carta2:
        valor2=7
    if "8" in carta2:
        valor2=8
    if "9" in carta2:
        valor2=9
    if "10" in carta2:
        valor2=10
    if "J" in carta2:
        valor2=10
    if "Q" in carta2:
        valor2=10
    if "K" in carta2:
        valor2=10
    suma=valor1+valor2
    print("Suma actual:", suma)
    pedir=input("¿Quieres pedir otra carta? (s/n) ").lower()
    while pedir=="s":
        numcar=random.randint(1,14)