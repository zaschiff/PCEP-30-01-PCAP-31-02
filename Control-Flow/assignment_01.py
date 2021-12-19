# Assignment 1

"""

Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True

"""

# Your Code Below:

def twelver(a, b):
    return ((a == 12) or (b == 12) or ((a + b) == 12))

print(twelver(3, 12))
print(twelver(4, 9))
print(twelver(9, 3))








































# Solution:
# def twelver(a, b):
#   return (a == 12 or b == 12 or a+b == 12)