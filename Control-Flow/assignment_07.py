# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

#Your Code Below:


def string_match(string1, string2):
    shorter = min(len(string1), len(string2))
    count = 0

    for i in range(shorter - 1):
        s1_sub = string1[i:i + 2]
        s2_sub = string2[i:i + 2]

        if s1_sub == s2_sub:
            count = count + 1

    return count


print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))































# Solution
# def string_match(a, b):
#     # Figure which string is shorter.
#     shorter = min(len(a), len(b))
#     count = 0
#
#     # Loop i over every substring starting spot.
#     # Use length-1 here, so can use char str[i+1] in the loop
#     for i in range(shorter - 1):
#         a_sub = a[i:i + 2]
#         b_sub = b[i:i + 2]
#         if a_sub == b_sub:
#             count = count + 1
#
#     return count
