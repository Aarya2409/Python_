# DSA Group 2: Arrays Intermediate - 4 Problems
# Building on basics—focus on searching, sorting, and multi-array ops. Keep rewriting code yourself, test thoroughly (include edges), and commit to GitHub.
# DSA Problem 4: Easy - Linear Search

# Problem: Given an array (e.g., [4, 2, 7, 1, 9]) and a target (e.g., 7), find if target exists, return index or -1.
# Coder's Thinking Process: 1. Loop through each element. 2. If match, return index. 3. End of loop: -1. 4. Time: O(n). 5. Edges: Target at start/end, not found, duplicates (return first).
# Sample Solution:

# Pythondef linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# arr = [4, 2, 7, 1, 9]
# target = 7
# print(linear_search(arr, target))  # 2

# Your Turn: Test with [1,3,5], target=2 (-1), commit "DSA: Arrays - Linear Search".

# DSA Problem 5: Easy-Medium - Binary Search (Sorted Array)

# Problem: Given sorted array (e.g., [1, 3, 5, 7, 9]) and target (e.g., 5), return index or -1.
# Coder's Thinking Process: 1. Assume sorted ascending. 2. Low=0, high=len-1. 3. While low <= high: mid = (low+high)//2, compare. 4. Adjust low/high. 5. Time: O(log n). 6. Edges: Not found, single element.
# Sample Solution:

# Pythondef binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# arr = [1, 3, 5, 7, 9]
# target = 5
# print(binary_search(arr, target))  # 2

# Your Turn: Test [2,4,6,8], target=9 (-1), commit.

# DSA Problem 6: Medium - Merge Two Sorted Arrays

# Problem: Given two sorted arrays (e.g., [1,3,5], [2,4,6]), merge into one sorted array.
# Coder's Thinking Process: 1. Init result list. 2. Two pointers i=0, j=0. 3. While both have elements: compare, append smaller, increment pointer. 4. Append remaining. 5. Time: O(m+n). 6. Edges: One empty, duplicates.
# Sample Solution:

# Pythondef merge_sorted(arr1, arr2):
#     result = []
#     i, j = 0, 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1
#     result.extend(arr1[i:])
#     result.extend(arr2[j:])
#     return result

# print(merge_sorted([1,3,5], [2,4,6]))  # [1,2,3,4,5,6]

# Your Turn: Test [], [1,2] ([1,2]), commit.

# DSA Problem 7: Medium - Rotate Array

# Problem: Rotate array right by k steps (e.g., [1,2,3,4,5], k=2 → [4,5,1,2,3]).
# Coder's Thinking Process: 1. k %= len (handle large k). 2. Reverse whole array, then first k, then rest. 3. Or slicing: arr[:] = arr[-k:] + arr[:-k]. 4. In place preferred. 5. Time: O(n). 6. Edges: k=0, k=len.
# Sample Solution:

# Pythondef rotate_array(arr, k):
#     n = len(arr)
#     k %= n
#     # Reverse all
#     arr.reverse()
#     # Reverse first k
#     arr[:k] = reversed(arr[:k])
#     # Reverse rest
#     arr[k:] = reversed(arr[k:])

# arr = [1,2,3,4,5]
# rotate_array(arr, 2)
# print(arr)  # [4,5,1,2,3]

# Your Turn: Test [7,8,9], k=1 ([9,7,8]), commit.