"""Given an array of ints, return True if 6 appears as either the
first or last element in the array. The array will be length 1 or more.
"""


def first_last6(nums):
    if nums[0] == 6:
        return True
    elif nums[len(nums) - 1] == 6:
        return True

    else:
        return False


#this is an optimal solution i came across
def first_last6(nums):
  return (nums[0]==6 or nums[-1]== 6)