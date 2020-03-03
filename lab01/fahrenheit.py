'''
Name: fahrenheit.py
Author: Anila Hoxha
Created: 02/03/2020
Description: Write a program that reads a Celsius degree in a float value from the
console, then converts it to Fahrenheit and displays the result. The formula for the
conversion is as follows: fahrenheit = (9 / 5) * celsius + 32
'''

celcius = input("Enter a degree in Celcius: ");
fahrenheit = (9.0/5.0) * float(celcius) + 32.0 # Calculate Fahrenheit value
print(str(fahrenheit) + " Fahrenheit")