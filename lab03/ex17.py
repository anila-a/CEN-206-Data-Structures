'''
Program: ex17.py
Author: Anila Hoxha
Last date modified: 03/13/2020

Write a Python program that inputs a list of words, separated by whitespace, and outputs how
many times each word appears in the list.
'''

def count(list):
    f = []
    for i in list:
        f.append(list.count(i))
    return f

s = str(input("Enter a list of words: "))
list = s.split()
print(count(list))
