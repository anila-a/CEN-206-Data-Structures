'''
Program: ex10.py
Author: Anila Hoxha
Last date modified: 03/11/2020

Write a short Python function that takes a sequence of integer values and determines if there is a
distinct pair of numbers in the sequence whose product is odd.
'''

def odd(list):
    flag = False
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if i != j:
                if int(list[i]) * int(list[i]) % 2 != 0: # If product is odd, assign True to flag
                    flag = True
    if flag:
        print("True")
    if not flag:
        print("False")

list = [2, 11, 33, 46, 52, 18]
odd(list)