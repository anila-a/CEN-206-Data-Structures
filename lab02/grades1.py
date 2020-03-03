'''
Name: grades1.py
Author: Anila Hoxha
Created: 03/03/2020
Description: Write a program that reads 5 students’ grades as input one by one, then it
prints the average grade of 5 students. (Use while loop)
'''

sum = 0.0
i = 5
while i > 0: # For i greater than 0, iterate through values
    grade = float(input("Enter the grade: "))
    sum += grade # Add grade to sum
average = sum / 5.0 # Calculate average
print("The average is " + str(float(average)))