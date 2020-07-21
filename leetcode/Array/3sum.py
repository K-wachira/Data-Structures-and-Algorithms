"""
source of solution **
:::https://leetcode.com/problems/3sum/discuss/7482/Fastest-Python-solution-180-ms

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.



"""


def threeSum( nums):
    res = []
    nums.sort()
    length = len(nums)
    for i in range(length - 2):  # [8]
        if nums[i] > 0: break  # [7]
        if i > 0 and nums[i] == nums[i - 1]: continue  # [1]

        l, r = i + 1, length - 1  # [2]
        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total < 0:  # [3]
                l += 1
            elif total > 0:  # [4]
                r -= 1
            else:  # [5]
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:  # [6]
                    l += 1
                while l < r and nums[r] == nums[r - 1]:  # [6]
                    r -= 1
                l += 1
                r -= 1
    print(res)
    return res
nums = [0,0,0,0]
threeSum(nums)