# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def twoSum(nums: [int], target: int) :
    for i in range(len(nums) - 1):
        if nums[i]+ nums[i + 1]== target:
            print(i)





nums = [3,3]
target = 6

twoSum(nums, target)