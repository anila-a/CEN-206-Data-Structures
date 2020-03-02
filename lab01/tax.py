""" Write a program that reads the purchase amount and calculates the sales tax
(6%). Display the tax with three digits after the decimal point. """

purchase = input("Enter the purchase amount: ")
print("Sales tax is " + str(float(purchase) * 6.0 / 100.0) + " LEK")
