"""
10. Write a Python program to reverse the order of
words in a given sentence.
Input_sentence = “Hello, World! Welcome to Python
programming.”
Output after reverse = “programming. Python to Welcome
World! Hello,”

"""



input_string = "programming. Python to Welcome World! Hello"
reverse_words = input_string.split()[::-1]
reverse_sentance = ' '.join(reverse_words)
print(f"sentance after reverse the sentance : {reverse_sentance}")