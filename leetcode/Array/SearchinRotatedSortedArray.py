
import math


def  search( nums, target):
    if len(nums) == 0: return -1

    pivot = min(nums)
    if target == pivot:
        print(nums.index(pivot))
        return nums.index(pivot)
    elif target == nums[0]:
        return 0
    elif target == nums[len(nums) - 1]:
        return len(nums) - 1
    elif target > pivot and target <= nums[len(nums) - 1]:
        number = binarysearch(target, nums[nums.index(pivot):])
        print(number)
        print(nums.index(number))
    elif target >= nums[0] and target <= nums[nums.index(pivot) - 1]:
        number = binarysearch(target, nums[: nums.index(pivot)])
        print(nums.index(number))


    else:
        return -1


def binarysearch( target, nums):
    middlepoint = int(len(nums) / 2)
    if target == nums[middlepoint]:
        return (middlepoint)
    elif target > nums[middlepoint]:
        binarysearch(target, nums[middlepoint:])
    elif target > nums[middlepoint]:
        binarysearch(target, nums[:middlepoint])







nums = [4,5,6,7,0,1,2]
target = 7

search(nums, target)