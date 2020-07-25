def partitionArray(nums):
    nums.sort()
    parta = []
    partb = []
    partc = []
    for i in nums:
        if (i % 2 == 0 and i % 3 == 0):
            parta.append(i)
        elif i % 2 == 0:
            parta.append(i)
        elif i % 3 == 0:
            partb.append(i)
        else:
            partc.append(i)

    parta.sort()
    partb.sort()
    partc.sort()
    nums.clear()
    nums.append(parta)
    nums.append(partb)
    nums.append(partc)

    return nums

nums=[2, 2, 3, 3]

print(partitionArray(nums))