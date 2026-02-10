nums=input()
if "       " in nums:
    nums.strip()
    num2=input()
    suma=11+22+int(num2)
elif " " in nums:
    listanum=nums.split()
    maximo=max(int(listanum[0]),int(listanum[1]), int(listanum[2]))
else:
    num2=input()
    num3=input()
    suma=int(nums)+int(num2)+int(num3)
print (suma)