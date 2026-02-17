#Write a program that, given two intervals, tells if one is inside the other, and computes the interval corresponding to their intersection, or tells that it is empty.


int1=input().split()
a=int(int1[0])
b=int(int1[1])
c=int(int1[2])
d=int(int1[3])
respuesta=""
if a==c and b==d:
        respuesta=respuesta+"="
elif a<=c and b>=d:
        respuesta=respuesta+"2"
elif c<=a and d>=b:
    respuesta=respuesta+"1"
else:
    respuesta=respuesta+"?"
if b<c or d<a:
        intervalo="[]"
elif a<=c and b>=d:
        intervalo="["+str(c)+","+str(d)+"]"
elif c<=a and d>=b:        
       intervalo="["+str(a)+","+str(b)+"]"
elif a<=c and b>=c and b<=d:
       intervalo="["+str(c)+","+str(b)+"]"
elif c<=a and d>=a and d<=b:
       intervalo="["+str(a)+","+str(d)+"]"
print(respuesta,",",intervalo)