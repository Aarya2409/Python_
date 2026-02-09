# Group 1: Basics (Variables, Data Types, Input/Output) - 3 Programs




# ********************************************************************************************************************



# Program 1: Easy - Temperature Converter

# Problem: Write a program that takes a temperature in Celsius from user input and converts it to Fahrenheit. Formula: F = (C * 9/5) + 32. Print the result with 2 decimal places.
# Coder's Thinking Process: 1. Understand input/output: Need float for temp (decimals possible). 2. Recall formula—test mentally (e.g., 0C = 32F). 3. Handle input as string, convert to float. 4. Format output nicely. 5. Edge cases: Negative temps, non-numbers (but skip error handling for easy level).
# Sample Solution:

# temp = float(input("enter the temp in celcius:"))

# fahrenhiet = (temp*9)/5 + 32

# print("temperature in fahrnheit is :",fahrenhiet)







# ********************************************************************************************************************





# Program 2: Easy-Medium - BMI Calculator

# Problem: Ask for user's weight (kg) and height (meters), calculate BMI = weight / (height ** 2). Print BMI and category: Underweight (<18.5), Normal (18.5-24.9), Overweight (25+).
# Coder's Thinking Process: 1. Inputs: Two floats. 2. Calc BMI—use ** for power. 3. Add if-elif for categories (decision-making preview). 4. Round BMI to 1 decimal. 5. Edges: Height=0 (but ignore for now), realistic values.

# weight = float(input("enter your wieght in kgs please:"))
# height = float(input("enter your height in meters please:"))

# bmi = weight / (height ** 2)

# print(f"your bmi is :{bmi:.1f}")

# if(bmi<18.5):
#     print("you are underweight ")
# elif(bmi < 24.9):
#     print(" you are normal")
# else:
#     print("You are overweight")



# ********************************************************************************************************************


# Program 3: Medium - Simple Interest Calculator

# Problem: Input principal amount, rate (%), time (years). Calc simple interest = (P * R * T)/100. Print total amount (principal + interest).
# Coder's Thinking Process: 1. Three inputs: floats for precision. 2. Formula straightforward—watch division. 3. Output both interest and total. 4. Edges: Zero rate/time. 5. Think reuse: Could make vars descriptive for clarity.


# p = float(input("enter your principal amount :"))

# r = float(input("enter your rate of interest :"))

# t = float(input("enter your time in years:"))
 
# interest = p*r*t/100
# total = p + interest
# print(f"total amount is {total}")


# print(f"your interest is {interest:.2f}")
# print(f"total amount is {total:.2f}")





# ********************************************************************************************************************
