def canJump(nums):
    if not nums: return True
    n = 0
    for i in range(len(nums)-1):
        if n == len(nums):
            print(True)
        elif n > len(nums):
            print(False)

        if nums[n]==0:
            print(False)
        else:
            n = nums



nums =  [2,3,1,1,4]
canJump(nums)