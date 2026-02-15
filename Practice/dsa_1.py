# DSA Group 1: Arrays Basics - 3 Problems
# Focus: Indexing, traversal, simple ops. Arrays in Python = lists.
# DSA Problem 1: Easy - Find the Maximum in an Array

# Problem: Given an array of integers (hardcode like [3, 1, 4, 1, 5]), find and print the maximum value.
# Coder's Thinking Process: 1. Assume non-empty array. 2. Init max_var to first element. 3. Loop through array, compare each to max_var, update if larger. 4. Built-in max() ok for easy, but practice manual loop. 5. Edges: All negative? Single element?
# Sample Solution:

# Pythonarr = [3, 1, 4, 1, 5]
# max_val = arr[0]
# for num in arr:
#     if num > max_val:
#         max_val = num
# print(max_val)  # Output: 5

# Your Turn: Rewrite, test with [-1, -5, -3] (max -1), commit "DSA: Arrays - Max Finder".

# DSA Problem 2: Easy-Medium - Reverse an Array

# Problem: Given an array (e.g., [1, 2, 3, 4]), reverse it in place (modify original) and print.
# Coder's Thinking Process: 1. Use two pointers: start=0, end=len-1. 2. Swap while start < end. 3. No extra space. 4. Edges: Even/odd length, empty.
# Sample Solution:

# Pythonarr = [1, 2, 3, 4]
# start = 0
# end = len(arr) - 1
# while start < end:
#     arr[start], arr[end] = arr[end], arr[start]
#     start += 1
#     end -= 1
# print(arr)  # [4, 3, 2, 1]

# Your Turn: Test [5,6], commit.

# DSA Problem 3: Medium - Remove Duplicates from Sorted Array

# Problem: Given a sorted array (e.g., [1,1,2,2,3]), remove duplicates in place, return new length, print modified array up to new length.
# Coder's Thinking Process: 1. Assume sorted ascending. 2. Two pointers: i for unique, j for traversal. 3. If arr[j] != arr[i], copy to i+1. 4. Return i+1. 5. Edges: All unique, all same, empty.
# Sample Solution:

# Pythonarr = [1,1,2,2,3]
# if not arr:
#     print(0)
# else:
#     i = 0
#     for j in range(1, len(arr)):
#         if arr[j] != arr[i]:
#             i += 1
#             arr[i] = arr[j]
#     print(arr[:i+1])  # [1,2,3]
#     print(i+1)  # 3

# Your Turn: Test [0,0,1,1,1,2,2], commit.