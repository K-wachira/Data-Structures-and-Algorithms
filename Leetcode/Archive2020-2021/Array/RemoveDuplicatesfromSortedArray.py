"""
::link https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

::
set index 0 or nums list to the min number

slice the list from index 0 - index(lensofar)

loop through the unsliced part of the list
if an element on the unsliced part of the list
is not in the sliced part of the list insert it to index lensofar
do this until there is no element in nums that is not in sliced part of nums

"""
def removeDuplicates(nums) :
    if len(nums) == 0: return 0
    lensofar = 1
    nums.insert(0, min(nums))

    for j in (nums[lensofar:]):
        if j not in (nums[:lensofar]):
            nums.insert(lensofar, j)
            lensofar += 1
    print(nums[:lensofar])
    return lensofar


nums =[-3,-1,0,0,0,3,3]
removeDuplicates(nums)