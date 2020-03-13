'''
Program: ex13.py
Author: Anila Hoxha
Last date modified: 03/13/2020

Python’s random module includes a function shuffle(data) that accepts a list of elements and
randomly reorders the elements so that each possible order occurs with equal probability. The
random module includes a more basic function randint(a, b) that returns a uniformly random
integer from a to b (including both endpoints). Using only the randint function, implement your
own version of the shuffle function.
'''

import random

def shuffle(list):
    for i in range(len(list)-1, 0, -1):
        n = random.randint(0, len(list)-1)
        list[i], list[n] = list[n], list[i]
    return list

list = [0, 1, 2]
print(shuffle(list))