"""
:: This is genius... Runtime is also not bad

:: Breakdown

for i in range(len(min(strs))) --> so as to iterate the minimum number of times

    c =strs[0][i] -->takes the first word on the list and the first letter of the word and assigns it to 'c'

    if all(a[i] == c for a in strs):
        :: all()--> returns true is all the values are same (true)
        :: a[i] == c for a in strs --> for all words(a) in str take a[i] with i being the index of the letters
        ::: so if all letters are the same
        prefix += c -->  add the letter to prefix
    else: break the loop and return the prefix so far

"""

def longestCommonPrefix( strs):
    prefix = ""
    if len(strs) == 0: return prefix
    for i in range(len(min(strs))):
        c = strs[0][i]
        if all(a[i] == c for a in strs):
            prefix += c
        else:
            break
    return prefix

strs = ["flower","flow"]

longestCommonPrefix(strs)