letra=str(input())
if letra.isupper():
    print("uppercase")
else:
    print("lowercase")
if letra in "AEIOU" or letra in "aeiou":
    print("vowel")
else:
    print("consonant")