#Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos
import statistics

num=int(input("Introduce el número de alumnos: "))
cata=[]   
ing=[]
caste=[]

for i in range(num):
    nota_cat=float(input(f"Introduce la nota de catalán del alumno {i+1}: "))
    nota_ing=float(input(f"Introduce la nota de inglés del alumno {i+1}: "))
    nota_cas=float(input(f"Introduce la nota de castellano del alumno {i+1}: "))
    cata.append(nota_cat)
    ing.append(nota_ing)
    caste.append(nota_cas)

medcat=sum(cata)/num
meding=sum(ing)/num
medcast=sum(caste)/num
medicat=statistics.median(cata)
mediing=statistics.median(ing)
medicast=statistics.median(caste)

print(f"Media de catalán: {medcat}, Mediana de catalán: {medicat}")
print(f"Media de inglés: {meding}, Mediana de inglés: {mediing}")
print(f"Media de castellano: {medcast}, Mediana de castellano: {medicast}")
