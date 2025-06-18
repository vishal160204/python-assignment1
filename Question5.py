"""
Write a Python program to find the factorial of a
number using a for loop.
"""


fact = 1
n = int(input("Enter a number : "))
for i in range(1,n+1):
    fact *= i
print(f"factorial of given number is : {fact}")