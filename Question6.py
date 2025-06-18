"""
6. Write a Python program to check if a given number
is a perfect number.
A Perfect number is a positive integer that is equal to the
sum of its proper divisors. For instance, 6 has divisors 1, 2,
and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
Input: 5
Output: No

"""


n = int(input("Enter a number : "))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum += i
if sum == n:
    print("Yes")
else:
    print("No")