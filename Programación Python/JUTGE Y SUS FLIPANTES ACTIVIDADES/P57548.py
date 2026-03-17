nums=input()
if " " in nums:
    listanum=nums.split()
    suma=int(listanum[0])+int(listanum[1])
else:
    num2=input()
    suma=int(nums)+int(num2)
print (suma)