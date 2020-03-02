""" Write a program that prompts the user to enter the distance to drive,
the fuel efficiency of the car in liters per 100km, and the price per liter, and displays the
cost of the trip. """

distance = input("Enter the driving distance: ")
liters = input("Enter liters per 100 km: ")
price = input("Enter price per liter (LEK): ")
print("The cost of driving is " + str((float(distance) / 100.0) * float(liters) * float(price)) + " LEK")
