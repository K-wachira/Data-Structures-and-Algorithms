from functools import reduce


def letterCombinations(digits):
    if '' == digits: return []
    kvmaps = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    ret = ['']
    for c in digits:
        print(c)
        tmp = []
        for y in ret:
            print(y)
            for x in kvmaps[c]:
                print(y+x)
                tmp.append(y + x)
        ret = tmp
    # print(ret)
    return ret

digits = '23'
letterCombinations(digits)