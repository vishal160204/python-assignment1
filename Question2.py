"""
2. Write a program that accepts a string as input from
the user and calculates the number of digits and
letters.
"""

alpha=0
num=0
for i in list("hello2123"):
    if i.isalpha():
        alpha += 1
    elif i.isnumeric():
        num += 1
print( f"total alphabets : {alpha}" )
print( f"total numbers : {num}")