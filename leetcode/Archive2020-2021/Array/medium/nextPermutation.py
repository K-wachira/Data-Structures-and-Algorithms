def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    shouldsort = True
    length = len(nums)-1
    print(nums)
    for i,n in enumerate(nums):
        last = nums[len(nums)-(i+1)]
        previous = nums[len(nums)-(i+2)]
        if last > previous:
            shouldsort = False
            first = nums[length - (i + 1)]

            second =nums[length - i]
            counta = length - (i + 1)
            tobeswappedwith = max(nums[length - (i + 1):])
            for i,n in enumerate(nums[length - (i + 1):]):
                if n > first :
                    counta += 1
                    tobeswappedwith = min(tobeswappedwith, n)
            nums[length - (i )] ,nums[counta]= nums[counta], nums[length - (i )]

            print(nums)
            print(nums[i])
            ReverseandSwap(nums,i )
            print(nums)



            break

    if shouldsort:
        nums.sort()
def ReverseandSwap(nums, start):
    end = len(nums)-1
    while start < end:
        nums[start] ,nums[end]= nums[end], nums[start]
        start+=1
        end-=1
    return nums



            # swap the two elements


nums = [1,5,0,0]
nextPermutation(nums)

# check if the last element is greater than the previous last, if so switch them up
#     else make the previous last to last
#
# check for the
#     list number that is more than the provided :
#     and if its equal move to the next one


#
# Take the first element and check
#     if minimum of the rest of the array if less than it ...if so switch them up :
#     if they are equal make them sit together
