palabras=input().split()

if len(palabras[0])>len(palabras[1]):
    print(palabras[0], " > ", palabras[1])
elif len(palabras[1])>len(palabras[0]):
    print(palabras[0], " < ", palabras[1])
else:
    print(palabras[0], " = ", palabras[1])