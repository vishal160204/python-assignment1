"""
Write a Python program to find the sum of all odd
numbers between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25

"""



sum = 0
for i in range(1,10):
    if i % 2 != 0:
        sum += i
print(f"sum of odd numbers b/w 1 to 10 is {sum}")