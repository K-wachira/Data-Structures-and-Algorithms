
def twoSum(nums, target):
    returnList =[]
    for i in nums:
        firstindex = nums.index(i)
        lookingFor = target - i
        nums.remove(i)
        if lookingFor in nums:
            nums.insert(firstindex,0.1)
            returnList.append(firstindex)
            returnList.append(nums.index(lookingFor))
            nums.insert(firstindex, i)
            return (returnList)


        else:
            nums.insert(firstindex,i)



target = 9
nums = [2,7,11,15]
twoSum(nums, target)