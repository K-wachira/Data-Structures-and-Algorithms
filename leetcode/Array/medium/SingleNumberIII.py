from collections import defaultdict
"""
https://leetcode.com/problems/single-number-iii/submissions/

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

"""

def singleNumber(nums):
    dublicateList = []
    dic = defaultdict(list)
    for index, number in enumerate(nums):
        dic[number].append(index)
    for i in dic:
        if len(dic[i]) ==1:
            dublicateList.append(i)
    return (dublicateList)


nums = [12]
print(singleNumber(nums))


