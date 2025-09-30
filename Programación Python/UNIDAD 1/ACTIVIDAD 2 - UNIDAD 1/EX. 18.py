#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.


precio=12

menores=int(input("Introduce el número de menores: "))
adultos=int(input("Introduce el número de adultos: "))

menores=menores*precio*0.5
adultos=adultos*precio*0.9
total=menores+adultos

print("El total a pagar es:", total)