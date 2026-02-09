# Group 2: Control Structures (Conditionals and Loops) - 4 Programs


# *******************************************************************************************************************************
# Build on decisions and repetition.
# Program 4: Easy - Vowel Checker

# Problem: Take a single character input, check if it's a vowel (a,e,i,o,u—A/E too). Print "Vowel" or "Consonant".
# Coder's Thinking Process: 1. Input as str, check length=1 (but assume valid). 2. Use if with or conditions, lower() for case-insensitivity. 3. Edges: Non-letter? Print "Invalid" as bonus.

# Sample Solution:

a = input("enter a chracter:").lower()

if a in 'aeiou':
    print("vowel")
else:
    print("consonant")
    

# *******************************************************************************************************************************
