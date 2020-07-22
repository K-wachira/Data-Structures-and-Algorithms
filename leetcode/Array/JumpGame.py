def canJump(nums):

    stepIndex = 0
    for index, number in enumerate(nums):
        if index > stepIndex:return False
        stepIndex = max(stepIndex, index+number)
    return True







nums =  [2,3,1,1,4]
print(canJump(nums))