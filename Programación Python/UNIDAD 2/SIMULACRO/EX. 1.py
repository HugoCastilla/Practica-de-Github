nums=input("Introduce las notas: ")
lista=nums.split(",")
print(lista)
lista=[int(x) for x in lista]
maxnum=max(lista)
minnum=min(lista)
lista.remove(minnum)
lista.remove(maxnum)
print(lista)
media=sum(lista)
media=round(media/8, 2)
if media>5 and media<10:
    print("Rendimiento medio")
elif media>=10:
    print("Rendimiento alto")
else:
    print("Rendimiento bajo")