'''
Name: histogram.py
Author: Anila Hoxha
Created: 03/03/2020
Description: Given the following array, display its data graphically by plotting each
numeric value as a bar of asterisk “ * ” as shown in table. (Use string repetition operator)
myArray = [2, 10, 12, 5, 1, 4, 0, 6, 19]
'''

myArray = [2, 10, 12, 5, 1, 4, 0, 6, 19]
string = "*"
print("Element\tValue\tHistogram")
for i in range(0, len(myArray), 1): # Iterate throught values
    print(str(i) + "\t\t" + str(myArray[i]) + "\t\t" + (string*myArray[i]))