"""

8. Write a Python program to calculate the LCM (Least
Common Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36

"""

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
for i in range(num1,(num1 * num2) + 1):
    if i % num1 == 0 and i % num2 == 0:
        print(f"LCM of 2 numbers is {i}")
        break