import math


def reverse( x):
    sign = ''
    strs = str(x)
    if strs[0] == '-' or strs[0] == '+':
        sign = strs[0]
        strs = strs[1:]
    new = ''
    counta = len(strs) - 1
    for j in range(len(strs)):
        new += str(strs[counta])
        counta -= 1
    new = sign + new

    if (int(new)) in range(int(math.pow(-2, 31)),
                           int(math.pow(2, 31) - 1)):
        return int(new)
    else:
        return 0