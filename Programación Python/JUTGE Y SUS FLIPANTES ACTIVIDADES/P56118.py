#Write a program that reads two numbers and prints their maximum.
nums=input()
if " " in nums:
    listanum=nums.split()
    maximo=max(int(listanum[0]),int(listanum[1]))
print(maximo)