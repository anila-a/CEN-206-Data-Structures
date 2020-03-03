'''
Name: table.py
Author: Anila Hoxha
Created: 03/03/2020
Description: Write a program that displays the following table:
a a^2 a^3
1  1   1
2  4   8
3  9   27
4  16  64
'''

print("a\ta^2\ta^3")
for i in range(1, 5, 1): # Iterate through values
    print(str(i) + "\t" + str(i ** 2) + "\t" + str(i ** 3))
