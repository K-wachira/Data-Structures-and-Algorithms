"""

The number 6 is a truly great number.
Given two int values, a and b, return True if either one is 6.
Or if their sum or difference is 6. Note: the function abs(num)
computes the absolute value of a number.

"""


def love6(a, b):
  sum = a +b
  difa = a -b
  difb =b-a
  return a == 6 or b == 6 or  sum ==6 or difa ==6 or difb ==6