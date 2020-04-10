'''
Program: countSubString.py
Author: Anila Hoxha
Last date modified: 04/10/2020

Write a recursive function that counts the number of times a string
occurs in another string. Hint: To get the rest of the string you can use s2[1:].
'''

def countSubString(str1, str2):
    s1 = len(str1)
    s2 = len(str2)

    if s1 == 0 or s1 < s2: # Base case
        return

    if str1[0: s2] == str2: # Check if the substring matches
        return countSubString(str1[s2 - 1:], str2) + 1

    return countSubString(str1[s2 - 1:], str2) # Return from the remaining string

str1 = str(input("Enter the first string: "))
str2 = str(input("Enter the second string: "))

print(countSubString(str1, str2))