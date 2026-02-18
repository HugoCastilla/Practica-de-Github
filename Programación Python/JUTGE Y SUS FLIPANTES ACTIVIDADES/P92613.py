import math
num=str(input())
if not num.isdecimal():
    num=float(num)
    decinf=int(num)
    decsup=int(num) + 1
    entera=int(num)
    decimal=num-entera
    if decimal >= 0.5:
        redondeo = entera + 1
    else:
        redondeo = entera
else:
    decinf = int(num)
    decsup = int(num) + 1
    redondeo = int(num)
print(decinf, decsup, redondeo)