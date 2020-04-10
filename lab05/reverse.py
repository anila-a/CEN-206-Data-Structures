'''
Program: reverse.py
Author: Anila Hoxha
Last date modified: 04/9/2020

Write a recursive function that displays a string reversely on the console
using the following function: def reverse(text):
'''

def reverse(text):
    if len(text) == 0:
        return 0
    s = text[0]
    reverse(text[1:]) # Recursive call, get the rest of the string as a parameter
    print(s, end = '')

text = str(input("Enter a text: "))
reverse(text)
