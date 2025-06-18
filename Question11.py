"""
11. Write a Python program to calculate the sum of
digits of a given number until the sum becomes a
single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced
to
on single digit.
Final Output: 6


"""



sum = 0
num = int(input("Enter a number : "))
while(num > 0):
    rem = num % 10
    sum += rem
    num = int(num / 10)
    if sum > 9:
        temp = sum
        sum = 0
        while(temp > 0):
            re = temp % 10
            sum += re
            temp = int(temp / 10)
print(sum)