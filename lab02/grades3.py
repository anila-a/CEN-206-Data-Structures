'''
Name: grades3.py
Author: Anila Hoxha
Created: 03/03/2020
Description: Write a program for this pseudocode:
'''

passes = 0
failures = 0
cnt = 1
while cnt <=10: # Iterate through ten values
    result = int(input("Enter result (1=pass, 2=fail): "))
    if(result == 1):
        passes += 1 # Increment passes if input == 1
    else:
        failures += 1 # Increment failures
    cnt += 1 # Increment counter
print("Passed: " + str(passes))
print("Failed: " + str(failures))
if passes > 8:
    print("Raise tuition")