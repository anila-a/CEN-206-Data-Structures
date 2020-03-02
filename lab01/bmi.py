weight = input("Enter the weight in pounds: ")
height = input("Enter the height in inches: ")

weight = float(weight) * 0.45359237
height = float(height) * 0.0254
print("BMI: " + str(weight / height ** 2))