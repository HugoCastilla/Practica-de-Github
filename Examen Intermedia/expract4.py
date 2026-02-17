valor=100

while valor>=50 and valor<=150:
    print("Valor actual:",valor)
    num=int(input("Ingrese un numero: "))
    if num<0:
        break
    if num%2==0:
        valor=valor/2
    else:
        valor=valor+num
    if num%3==0:
        valor=valor-5
print("Proceso terminado. Valor final:",valor)
    