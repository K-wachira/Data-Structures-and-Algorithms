"""

You and your date are trying to get a table at a restaurant.
The parameter "you" is the stylishness of your clothes, in the range
0..10, and "date" is the stylishness of your date's clothes. The result
getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes.
If either of you is very stylish, 8 or more, then the result is 2 (yes).
With the exception that if either of you has style of 2 or less, then the
result is 0 (no). Otherwise the result is 1 (maybe).

"""

def date_fashion(you, date):
  if you >= 8 and date >2 or you > 2 and date >= 8:
    return 2
  elif you <= 2 or date <=2 :
    return 0
  else:
    return 1