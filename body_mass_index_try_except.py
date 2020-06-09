#!/usr/bin/env python3

#basic procedural program used to calculate BMI. Implements try/except block to account for bad user input

print("Welcome to the Body Mass Index Caclulator")
print()

print("Please note this BMI calculator uses the American System")
print()

#use exception handling to account for bad height input
while True:
    try:
        height = int(input("Please enter your height in inches: "))
        print()
    except ValueError:
        print("Error. Height must be an integer. Please try again: ")
        print()
        continue
    if height <= 0:
        print("Error. Height must be greater than 0. Please try again: ")
        print()
        continue
    else:
        break

#use exception handling to account for bad weight input
while True:
    try:
        weight = int(input("Please enter your weight in pounds: "))
        print()
    except ValueError:
        print("Error. Weight must be an integer. Please try again: ")
        print()
        continue
    if height <= 0:
        print("Error. Weight must be greater than 0. Please try again: ")
        print()
        continue
    else:
        break

#calculate BMI
BMI = round(float((weight/height/height) * 703),2)
print("Your BMI is: ", BMI)

#Give user their BMI category based on calculated BMI
if BMI < 18.5:
    print("You are considered underweight")
elif BMI >= 18.5 and BMI < 25:
    print ("You are considered normal weight")
elif BMI >= 25 and BMI < 30:
    print ("You are considered overweight")
else:
    print ("You are considered obese")
    
print()
print("Thank you for using the BMI Calculator")
