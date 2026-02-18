nums=input()
if " " in nums:
    listanum=nums.split()
    maximo=max(int(listanum[0]),int(listanum[1]), int(listanum[2]))
print(maximo)