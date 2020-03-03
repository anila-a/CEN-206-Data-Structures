'''
Name: bmi.py
Author: Anila Hoxha
Created: 02/03/2020
Description: Body Mass Index (BMI) is a measure of health on weight. It can be calculated
by taking your weight in kilograms and dividing by the square of your height in meters.
Write a program that prompts the user to enter a weight in pounds and height in
inches and displays the BMI. Note that one pound is 0.45359237 kilograms and one
inch is 0.0254 meters.
'''

weight = input("Enter the weight in pounds: ")
height = input("Enter the height in inches: ")

weight = float(weight) * 0.45359237 # Convert pounds to kilograms
height = float(height) * 0.0254 # Convert inches to meters
print("BMI: " + str(weight / height ** 2))