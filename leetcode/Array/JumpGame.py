def canJump(nums):
    target  = len(nums)
    n = 0


    while n  <= target:
        print("nunu")
        n = n + nums[n]
        if n == target:
            print("Found")
        elif n > target:
            print(False)

    print(False)




nums = [2,3,1,1,4]
canJump(nums)