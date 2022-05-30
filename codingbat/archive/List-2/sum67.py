
def sum67(nums):
    sum = 0
    counting = True  #boolian indicating if it should be counting


    for i in nums:
        if i == 6: # when i is six counting is turned off
            counting = False
        if counting:
            sum += i
        if i == 7: #if counting is 7 counting is turned on again
            counting = True
    return sum


print(sum67([6, 7, 1, 6, 7, 7]))

