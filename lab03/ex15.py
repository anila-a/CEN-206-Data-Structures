'''
Program: ex15.py
Author: Anila Hoxha
Last date modified: 03/13/2020

Write a short Python function that takes a string s, representing a sentence, and returns a copy of
the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this
function would return "Lets try Mike".
'''

def remove(s, p):
    for n in p:
        if n in s:
            s = s.replace(n, '')
    return s

s = "Let's try, Mike."
p = "!?.,(){}[]:;-_\'\"/\\"
print(remove(s, p))