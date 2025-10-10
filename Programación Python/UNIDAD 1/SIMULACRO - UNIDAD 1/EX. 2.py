frase=input("Introduzca una frase: ")
num1=int(input("Introduce un número: "))
num2=int(input("Introduce otro número: "))
num3=int(input("Introduce otro número: "))

#frase
fraseminus=frase.lower()

print(fraseminus)

#numeros
suma=num1+num2+num3

media=(num1+num2+num3)/3
mediaredondeada=round(media,2)

multi=num1*num2*num3

print("La suma es:", suma)
print("La media es:", mediaredondeada)
print("El producto es:", multi)

if suma>multi:
    print("La suma es mayor que el producto")
elif multi>suma:
    print("El producto es mayor que la suma")
else:
    print("La suma y el producto son iguales")




