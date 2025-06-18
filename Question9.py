"""
9. Write a Python program to count the frequency of
each element in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
"""



input_list = [1, 2, 3,2, 4, 1, 2, 4, 5]
Frequency = {}
for item in input_list:
    if item in Frequency:
        Frequency[item] += 1
    else:
        Frequency[item] = 1
print("Frequncy count : ", Frequency)  