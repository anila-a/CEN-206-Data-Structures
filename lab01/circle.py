'''
Name: circle.py
Author: Anila Hoxha
Created: 02/032/2020
Description: Write a program that displays the area and perimeter of a circle that has a
radius of 5.5 using the following formula: (Hint: “import math” for “pi”at first)
perimeter = 2 * radius * pi
area = radius * radius * pi
'''

import math

radius = 5.5
print ("The perimeter is: " + str(2 * radius * math.pi)) # Print perimeter
print("The area is: " + str(radius ** 2 * math.pi)) # Print area