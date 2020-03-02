distance = input("Enter the driving distance: ")
liters = input("Enter liters per 100 km: ")
price = input("Enter price per liter (LEK): ")
print("The cost of driving is " + str((float(distance) / 100.0) * float(liters) * float(price)) + " LEK")