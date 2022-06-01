"""
https://leetcode.com/problems/single-number-iii/submissions/

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once.

"""
def singleNumber(nums):
    nonDublicates = set()
    for i in nums:
        if i in nonDublicates:
            nonDublicates.discard(i)
        else:
            nonDublicates.add(i)
    return list(nonDublicates)
nums = [1,2,1,3,2,5]
print(singleNumber(nums))