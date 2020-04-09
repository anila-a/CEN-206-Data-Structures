'''
Program: hw1_2.py
Author: Anila Hoxha
Last date modified: 04/2/2020

Consider the Fibonacci function, F(n), which I defined such that
𝐹(1) = 1, 𝐹(2) = 2, 𝑎𝑛𝑑 𝐹(𝑛) = 𝐹(𝑛 − 2) + 𝐹(𝑛 − 1) 𝑓𝑜𝑟 𝑛 > 2.
Describe an efficient algorithm for determining first n Fibonacci numbers. What is the running time of
your algorithm, “Big-Oh”?
'''

def fibonacci(n):
    a = 0 # O(1)
    b = 1 # O(1)
    if n == 1: # O(1)
        print(a)
    elif n == 2: # O(1)
        print(a)
        print(b)
    else: # O(1)
        print(a)
        print(b)
        for i in range(3, n+1): # O(n)
            c = a + b # O(n)
            print(c) # O(n)
            # Exchange values for incrementation
            a = b # O(n)
            b = c # O(n)

n = int(input("Enter the value of n: ")) # O(1)
fibonacci(n)