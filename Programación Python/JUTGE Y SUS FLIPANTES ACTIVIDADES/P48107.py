num1=int(input())
num2=int(input())
if num1>num2:
    d=num1//num2
    div=num1%num2
else:
    d=num2//num1
    div=num2%num1
print(d,div)
