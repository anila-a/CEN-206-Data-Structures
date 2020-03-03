'''
Name: total.py
Author: Anila Hoxha
Created: 03/03/2020
Description: Write a program that that prompts the user to enter an integer “n” between 1
to 100 then displays the sum of first n numbers.
'''

n = int(input("Enter an integer between 1 to 100: "))
sum = 0
for i in range(1, n+1, 1): # Iterate through values
    sum += i # Add i to sum
print("Sum of numbers from 1 to " + str(n) + " is " + str(sum))