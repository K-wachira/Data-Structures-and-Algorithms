
"""
:: THIS APPROACH DOES NOT MATTER WHAT LETTERS BEGIN
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