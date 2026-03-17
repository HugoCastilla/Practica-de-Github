t=input().split()
h=int(t[0])
m=int(t[1])
s=int(t[2])

s=s+1
if s==60:
    s=0
    m=m+1
if m==60:
    m=0
    h=h+1
if h==24:
    h=0
print(h,m,s)