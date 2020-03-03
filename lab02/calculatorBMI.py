'''
Name: calculatorBMI.py
Author: Anila Hoxha
Created: 03/03/2020
Description: Body Mass Index (BMI) is a measure of health on weight. It can be
calculated by taking your weight in kilograms and dividing by the square of your height
in meters. Write a program that prompts the user to enter a weight and height then
displays the BMI.
'''

weight = float(input("Enter your weight in KG: "))
height = float(input("Enter your heigh in meter: "))
bmi = weight / (height ** 2) # Calculate BMI
if(bmi < 18.5):
    print("Your weight status is Underweight")
elif (18.5 <= bmi < 25.0):
    print("Your weight status is Normal")
elif (25.0 <= bmi < 30.0):
    print("Your weight status is Overweight")
else:
    print("Your weight status is Obese")
