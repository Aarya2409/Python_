# DSA Group 3: Strings Basics - 4 Problems
# Shifting to strings—common in interviews, builds on arrays (strings are char arrays). Use Python strings/lists for manipulation. Keep rewriting, testing, committing.
# DSA Problem 8: Easy - Reverse a String

# Problem: Given a string (e.g., "hello"), reverse it and return the new string.
# Coder's Thinking Process: 1. Strings immutable—use slicing [::-1] or loop backward. 2. For practice, manual loop to build new string. 3. Time: O(n). 4. Edges: Empty, single char, palindrome.
# Sample Solution:

# Pythondef reverse_string(s):
#     rev = ''
#     for char in s:
#         rev = char + rev
#     return rev

# print(reverse_string("hello"))  # "olleh"

# Your Turn: Test "world" ("dlrow"), commit "DSA: Strings - Reverse".

# DSA Problem 9: Easy-Medium - Check Palindrome

# Problem: Given a string (e.g., "radar"), check if it's a palindrome (ignore case, no spaces/punctuation for simplicity).
# Coder's Thinking Process: 1. Lowercase it. 2. Compare s == s[::-1]. 3. Or two pointers from ends toward center. 4. Time: O(n). 5. Edges: "A", empty, mixed case.
# Sample Solution:

# Pythondef is_palindrome(s):
#     s = s.lower()
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# print(is_palindrome("radar"))  # True

# Your Turn: Test "Racecar" (True), "hello" (False), commit.

# DSA Problem 10: Medium - Longest Substring Without Repeating Characters

# Problem: Given a string (e.g., "abcabcbb"), find length of longest substring without repeats (e.g., "abc" = 3).
# Coder's Thinking Process: 1. Sliding window: left/right pointers. 2. Set for unique chars in window. 3. If repeat, move left, remove from set. 4. Track max length. 5. Time: O(n). 6. Edges: All unique, all same, empty.
# Sample Solution:

# Pythondef longest_unique_substring(s):
#     char_set = set()
#     left = 0
#     max_len = 0
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)
#     return max_len

# print(longest_unique_substring("abcabcbb"))  # 3

# Your Turn: Test "pwwkew" (3, "wke"), commit.

# DSA Problem 11: Medium - String to Integer (atoi)

# Problem: Convert string to int (e.g., "42" → 42, "   -42" → -42). Handle leading whitespace, signs, ignore after non-digits. Clamp to 32-bit int range (-2^31 to 2^31-1).
# Coder's Thinking Process: 1. Strip whitespace. 2. Check sign, start index. 3. Build num until non-digit. 4. Clamp if out of range. 5. Time: O(n). 6. Edges: "words", overflow, no digits.
# Sample Solution:

# Pythondef my_atoi(s):
#     s = s.strip()
#     if not s:
#         return 0
#     sign = 1
#     i = 0
#     if s[0] == '-':
#         sign = -1
#         i += 1
#     elif s[0] == '+':
#         i += 1
#     num = 0
#     while i < len(s) and s[i].isdigit():
#         num = num * 10 + int(s[i])
#         i += 1
#     num *= sign
#     INT_MIN, INT_MAX = -2**31, 2**31 - 1
#     if num < INT_MIN:
#         return INT_MIN
#     if num > INT_MAX:
#         return INT_MAX
#     return num

# print(my_atoi("42"))  # 42
# print(my_atoi("   -42"))  # -42
# print(my_atoi("4193 with words"))  # 4193