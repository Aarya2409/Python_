# Program 8: Easy - List Sum and Average

# Problem: Hardcode a list of 5 numbers. Calc sum and average, print both.
# Coder's Thinking Process: 1. List init. 2. Use sum() built-in or loop. 3. Avg = sum/len. 4. Edges: Empty list? Skip.
# Sample Solution:

# nums = [1,2,3,4,5]

# total = sum(nums)

# average = total/len(nums)

# print(f"Sum:{total},average:{average}")



# ******************************************************************************************************


# Program 9: Easy-Medium - Dictionary Student Grades

# Problem: Create dict with 3 subjects:grades. Input a subject, print grade if exists, else "Not found".
# Coder's Thinking Process: 1. Dict init. 2. Input key, use get() or if in. 3. Case-sensitive? Lower inputs.
# Sample Solution:

# Pythongrades = {'Math': 90, 'Science': 85, 'English': 95}
# subject = input("Enter subject: ")
# if subject in grades:
#     print(f"Grade: {grades[subject]}")
# else:
#     print("Not found")

# Your Turn: Test 'Math' (90).

# Program 10: Medium - Remove Duplicates from List

# Problem: Input comma-separated numbers (e.g., "1,2,2,3"), convert to list, use set to remove dups, print sorted unique list.
# Coder's Thinking Process: 1. Input str, split(','), int convert in loop. 2. Set for uniques. 3. Sort list(output). 4. Edges: Empty, non-nums.
# Sample Solution:

# Pythoninput_str = input("Enter numbers (comma-separated): ")
# num_list = [int(x) for x in input_str.split(',')]  # Simple comprehension ok here
# unique = sorted(set(num_list))
# print(unique)

# Your Turn: Test "1,2,2,3" ([1,2,3]).


inputnums = input("enter the number with commas , : ")

tempset = [int(x) for x in inputnums.split(',')]
unique = sorted(set(tempset))
print(unique)



# Program 11: Medium - Tuple Max/Min

# Problem: Hardcode tuple of numbers. Find max, min, print them.
# Coder's Thinking Process: 1. Tuple immutable—use max/min built-ins. 2. Or loop manually. 3. Edges: Single element.
# Sample Solution:

# Pythonnums = (5, 3, 8, 1, 9)
# print(f"Max: {max(nums)}, Min: {min(nums)}")

# Your Turn: Add loop version if you want.

# Group 4: Functions - 4 Programs
# Modularize code.
# Program 12: Easy - Greeting Function

# Problem: Define function greet(name, location). Print "Hello [name] from [location]". Call with inputs.
# Coder's Thinking Process: 1. Def with params. 2. Call with inputs. 3. Reuse potential.
# Sample Solution:

# Pythondef greet(name, location):
#     print(f"Hello {name} from {location}")
# name = input("Name: ")
# loc = input("Location: ")
# greet(name, loc)

# Your Turn: Test "Aryan", "Manchester".

# Program 13: Easy-Medium - Even/Odd Function

# Problem: Function is_even(n) returns True/False. Call in loop for 1-10, print evens.
# Coder's Thinking Process: 1. Def return bool (n%2==0). 2. Loop calls it. 3. Edges: 0.
# Sample Solution:

# Pythondef is_even(n):
#     return n % 2 == 0
# for i in range(1, 11):
#     if is_even(i):
#         print(i)

# Your Turn: Test.

# Program 14: Medium - Palindrome Checker Function

# Problem: Function is_palindrome(word) checks if word == word[::-1]. Input word, print yes/no.
# Coder's Thinking Process: 1. Slicing for reverse. 2. Lower for case. 3. Edges: Empty, single char.
# Sample Solution:

# Pythondef is_palindrome(word):
#     word = word.lower()
#     return word == word[::-1]
# word = input("Enter word: ")
# print("Yes" if is_palindrome(word) else "No")

# Your Turn: Test "radar" (Yes).

# Program 15: Medium - List Reverse Function

# Problem: Function reverse_list(lst) returns reversed list (no reverse()). Call with sample.
# Coder's Thinking Process: 1. Loop backward or slicing. 2. New list. 3. Edges: Empty.
# Sample Solution:

# Pythondef reverse_list(lst):
#     return lst[::-1]  # Or loop: new = [] for i in range(len(lst)-1, -1, -1): new.append(lst[i])
# print(reverse_list([1,2,3,4]))

# Your Turn: Test [5,4,3] ([3,4,5]).