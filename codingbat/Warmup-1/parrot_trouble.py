"""
We have a loud talking parrot. The "hour" parameter is the current hour
 time in the range 0..23. We are in trouble if the parrot is talking and
  the hour is before 7 or after 20. Return True if we are in trouble.

"""

def parrot_trouble(talking, hour):
  if not talking:
    return False
  elif talking and hour < 7 :
    return True
  elif talking and hour >20:
    return True
  elif hour >= 7 and hour <= 20:
    return False
