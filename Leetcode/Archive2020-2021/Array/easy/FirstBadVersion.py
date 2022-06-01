
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

"""

def firstBadVersion(n):
    # nums = [i for i in range(1,n+1)]
    # print(nums)
    # for i,n in enumerate(nums):
    #    if not isBadVersion(i-1) and (isBadVersion(n) and isBadVersion(i+1)):
    #        return (n)


    # low , high = 0, len(nums)-1
    #
    # while low <= high :
    #     mid = (low+high)//2
    #
    #     if isBadVersion(nums[mid-1]) and isBadVersion(nums[mid]):
    #         high = mid-1
    #     elif not isBadVersion(nums[mid]) and not isBadVersion(mid+1):
    #         low =mid
    #     elif not isBadVersion(nums[mid-1]) and isBadVersion(nums[mid]) and isBadVersion(nums[mid+1]):
    #         return nums[mid]

        #
        # check if mid and mid -1 are bad .. if so go to lowwer bunk
        #
        # if mid and mid +1 are good go to upper bank
        #
        # if mid -1 is good , mid is bad and mid +1 is bad: return mid
    low=1
    high=n
    while low<high:
        mid=low+((high-low)//2)
        if isBadVersion(mid):
            high=mid
        else:
            low=mid+1
    return low

        # check if version half is bad ... and version half -1 is bad : if so n will be half -1
        #
        # check if version half is bad and version half -1 is good and return version half


def isBadVersion(x):
    if x >= 6: return True




 # populate a list with 1...n chars
 # create a for loop n times,
 #    check if n//2 is true
 #    if true check bottom half with the n included
 #    if false check upper half with n excluded

n = 15

print(firstBadVersion(n))