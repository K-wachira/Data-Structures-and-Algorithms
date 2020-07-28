def firstMissingPositive(nums):
    if not nums: return 1
    nums.sort()

    counta = 1
    for  n in (set(nums)):
        if n > 0:
            if n != counta:
                return counta
            counta += 1
        if sum(nums) < 1: return 1
    return max(nums) + 1
            





if __name__ == '__main__':
    listelements = [int(k) for k in input().split()]
    print(firstMissingPositive(listelements))



