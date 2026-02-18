#Write a program that, given two intervals, tells if one is inside the other. if one is inside the other, print "1". Otherwise, print "?". If they are the same print "="

int1=input().split()
a=int(int1[0])
b=int(int1[1])
c=int(int1[2])
d=int(int1[3])
if a==c and b==d:
        print("=")
elif a<=c and b>=d:
        print("2")
elif c<=a and d>=b:
        print("1")
else:
        print("?")