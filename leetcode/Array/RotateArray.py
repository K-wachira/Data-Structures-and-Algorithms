"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Link :: https://leetcode.com/problems/rotate-array/

steps ::
loop though the list k times
On each loop take the last element and insert it to index 0
pop the last element which has been duplicated on index 0

"""


def rotate( nums ,k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        lastElement = nums[len(nums) - 1]
        print(lastElement)
        nums.insert(0, lastElement)
        nums.pop()
        print(nums)

nums =  [1,2,3,4]
k = 3
rotate(nums, k)
