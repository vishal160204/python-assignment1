"""
7. Write a Python program to check if a string is an
anagram of another string.
string1 = "listen", string2 = "silent"
Output: True


"""


str1 = input("Enter your first string : ")
str2 = input("Enter your second string: ")
y= sorted(str1) == sorted(str2)
print(y)