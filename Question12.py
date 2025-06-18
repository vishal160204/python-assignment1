"""
12. Write a Python program to reverse a number using
a while loop.
Sample Input: num = 12345
Sample Output: revnum = 54321
"""

revnum = 0
num = int(input("Enter a number : "))
while(num > 0):
    rem = num % 10
    revnum = (revnum * 10) + rem
    num = int(num / 10)
print(f"reverse of number is  {revnum}")