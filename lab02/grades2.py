'''
Name: grades2.py
Author: Anila Hoxha
Created: 03/03/2020
Description: Write a program that reads student grades until user presses “-1”. Then
prints the average of the entered students. (Use while loop)
'''

sum = 0.0
grade = float(input("Enter the grade: "))
sum += grade
cnt = 1.0
while 1: # While true
    grade = float(input("Enter the grade: "))
    if grade == -1: # Check if grade is equal to -1
        break # Break the loop
    sum += grade
    cnt += 1 # Increment counter
average = sum / cnt # Calculate average
print("The average of " + str(cnt) + " students is " + str(float(average)))
