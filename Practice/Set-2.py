# Group 2: Control Structures (Conditionals and Loops) - 4 Programs


# *******************************************************************************************************************************
# Build on decisions and repetition.
# Program 4: Easy - Vowel Checker

# Problem: Take a single character input, check if it's a vowel (a,e,i,o,u—A/E too). Print "Vowel" or "Consonant".
# Coder's Thinking Process: 1. Input as str, check length=1 (but assume valid). 2. Use if with or conditions, lower() for case-insensitivity. 3. Edges: Non-letter? Print "Invalid" as bonus.

# Sample Solution:

# a = input("enter a chracter:").lower()

# if a in 'aeiou':
#     print("vowel")
# else:
#     print("consonant")


# *******************************************************************************************************************************


# Program 5: Easy-Medium - Number Guessing Game

# Problem: Generate a random number 1-10 (use import random). User guesses until correct. Print "Too high/low" hints, count attempts.
# Coder's Thinking Process: 1. Import random—randint(1,10). 2. While loop for guesses. 3. If-elif for hints. 4. Count with var. 5. Edges: Non-int input (skip handling).
# Sample Solution:

# import random 

# number = random.randint(1,10)
# attempts = 0

# while True:
#     guess = int(input("Guess a number between 1-10:"))
#     attempts +=1
#     if guess< number:
#         print("higher number")
#     elif guess > number:
#         print(" Lower number")
#     else:
#         print(f"bulls eys ! , in {attempts}")
#         break


# *******************************************************************************************************************************



# Program 6: Medium - Factorial Calculator

# Problem: Input positive integer, calculate factorial (e.g., 5! = 120) using a loop. Print result.
# Coder's Thinking Process: 1. Input int, assume positive. 2. For loop from 1 to n, multiply accumulatively. 3. Init fact=1. 4. Edges: 0! =1, large n (but ok for small).
# Sample Solution:

# number = int(input("enter the number you want factorial:"))

# fact = 1

# for i in range(1,number+1):
#     fact *= i
# print(f"the factorial of the number you entered is :{fact}")



# *******************************************************************************************************************************



# Program 7: Medium - Prime Number Checker

# Problem: Input number, check if prime (divisible only by 1 and itself). Print yes/no.
# Coder's Thinking Process: 1. Input int >1. 2. For loop 2 to sqrt(n) (optimize later), check %==0. 3. Flag var for prime. 4. Edges: 1/2/negatives.
# Sample Solution:

number = int(input("enter the number:"))

if number<=1:
    print("not prime")
else:
    is_prime = True
    for i in range(2,number):
        if number%2 == 0:
            is_prime = False
            break
    print("prime" if is_prime else "not prime")