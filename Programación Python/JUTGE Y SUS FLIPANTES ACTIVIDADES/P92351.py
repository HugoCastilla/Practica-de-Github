nums=input()
listanum=nums.split()
num1=int(listanum[0])
num2=int(listanum[1])
d=0
div=0
if num1 and num2!=0:
    d=num1//num2
    div=num1%num2
    print(d,div)
elif num1==0 or num2==0:
    print(0,0)
elif num1==0 and num2==0:
    print(0,0)