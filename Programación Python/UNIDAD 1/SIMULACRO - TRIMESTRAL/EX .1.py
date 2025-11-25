inicio=int(input("Introduce el primer valor del intervalo: "))
fin=int(input("Introduce el segundo valor del intervalo: "))
incremento=int(input("Introduce el incremento: "))

if incremento==0:
    print("El incremento no puede ser 0.")
else:
    if incremento>0:
        stop = fin+1
    else:
        stop = fin-1

    for n in range(inicio, stop, incremento):
        if n %  4!=0:
            if n%6==0:
                print(f"*{n}*", end=' ')
            else:
                print(n, end=' ')