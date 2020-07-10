"""
::: https://leetcode.com/problems/remove-element/submissions/

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

"""


def removeElement(nums, val):
    for i in range(len(nums) ):
        if val in nums:
            nums.remove(val)
    return len(nums)
nums = [1]
val = 1
removeElement(nums, val)