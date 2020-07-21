def has22(nums):
    nums.append(0)
    for index, number in enumerate(nums):
        if number == 2 and nums[index+1] ==2:
            return True
    return False


nums= [2,0,2]
print(has22(nums))