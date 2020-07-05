
"""
:: THIS APPROACH DOES NOT MATTER WHAT LETTERS BEGIN

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

On this solution it finds the biggest common substring that is in all the words without
considering where it is located on the strings.
NB if strs = ['ca', 'a] return is supposed to be ''
    but this function returns 'a' which is the longest substring on strs
see LongestCommonPrefix2.py for the correct function/approach

"""


def longestCommonPrefix( strs):
    smallest =(min(strs, key=len))
    lastLetter = 0
    longest = 0
    longeststr =['']

    for i in range(len(smallest)):
        for j in range(len(smallest)):
            lastLetter = lastLetter +1
            cah =all(chv(smallest[i:lastLetter], strs))
            if cah:
                longeststr.append(smallest[i:lastLetter])


        lastLetter = 1
    print(max(longeststr, key=len))

    return (max(longeststr, key=len))


def chv (i, strs):
    answers = []
    for j in range(len(strs)):
        if i in strs[j]:
            answers.append(True)
        else:
            answers.append(False)
    return answers

strs = ["flower","flow"]

longestCommonPrefix(strs)