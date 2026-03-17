listanum=[]
listanonum=[]
listatodo=[]

frase=input("Introduce valores separados por un guión: ")

listatodo=frase.split("-")

qfor x in range(len(listatodo)):
    if listatodo[x].isnumeric():
        listanum.append(int(listatodo[x]))
    else:
        listanonum.append(listatodo[x])

for x in listatodo:
    if x.isnumeric():
        listanum.append(int(listatodo[x]))
    else:
        listanonum.append(listatodo[x])

print(listanum)

print (sum(listanum))