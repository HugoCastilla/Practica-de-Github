#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
bmayor=float(input("Introduce la base mayor del trapezio: "))
bmenor=float(input("Introduce la base menor del trapezio: "))
altura=float(input("Introduce la altura del trapezio: "))
lados=float(input("Introduce la medida de los lados del trapezio: "))

perimetro=(lados*2)+bmayor+bmenor
area=((bmenor+bmayor)*altura)/2

print("El perímetro del trapezio es", perimetro)
print("El área del trapezio es", area)