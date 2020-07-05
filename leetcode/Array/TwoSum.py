"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

:: Approach

Assume the first number is 'i' , this makes the second number target - i
before searching for second number in nums list replace i with a placeholder
    (number that cant be second  number eg 0.1) in order to maintain the indexing of the numbers
if number is found append its index and that of i

Else Replace the placeholder( fake number) with its original value with is i



"""

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