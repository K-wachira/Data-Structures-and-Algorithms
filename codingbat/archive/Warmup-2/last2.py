"""
Given a string, return the count of the number of times that a substring
 length 2 appears in the string and also as the last 2 chars of the
 string, so "hixxxhi" yields 1 (we won't count the end substring).


"""


def last2(str):
    count = 0
    c = 0
    empty = []
    another = []
    ret = 0

    last = [(str[len(str) - 2:len(str)])]
    for i in str:
        count += 1
        if count < len(str):
            empty.append([i + str[count]])

    for i in empty:
        if i == last:
            ret += 1

    if ret - 1 < 0:
        return 0
    else:

        return (ret - 1)