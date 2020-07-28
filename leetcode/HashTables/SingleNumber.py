"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


def singleNumber(nums): # for every element apprears twice except one
    unique = set()
    for i in nums:
        if i in unique:
            unique.discard(i)
        else:
            unique.add(i)
    print(unique)
    return list(unique)[0]

def singleNumber2(nums): # For every element apprears more than once except one
    dic = {}
    for i in (nums):
        dic[i] =dic.get(i,0)+1
    for k,v in dic.items():
        if v == 1:
            return k

def singleNumber3(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

nums = [4,1,2,1,2,1]

# print(singleNumber(nums))
# print(singleNumber2(nums))
print(singleNumber3(nums))