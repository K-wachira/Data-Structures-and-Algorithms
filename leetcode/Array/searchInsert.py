"""
https://leetcode.com/problems/search-insert-position/submissions/

Time complexity = O(nlogn)
Binary search approach

"""

def searchInsert(nums, target):
    if not nums: return 0
    low, high = 0, len(nums)-1
    if target < nums[low]: return 0
    elif target > nums[high]: return high+1


    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:  return mid

        if nums[mid]< target < nums[mid+1]: return  mid+1


        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1




nums = []
target = 9
searchInsert(nums, target)