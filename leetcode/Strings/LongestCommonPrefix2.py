"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

This function works proper,

:: Approach 
Create a nested list(tuple) with the tuple containing letters that are on the same index
on the words on strs.

On the for loop if set of the tupple is one means the letters  are all the same hence append to returnString
and when set != 1 means that the letters on that tupple are not the same hence break the loop as the common prefix
ends there.


"""


def longestCommonPrefix(strs):
    l = list(zip(*strs))
    returnString =''
    print(l)

    for i in l:
        if len(set(i))== 1:
            returnString = returnString + i[0]
        else:
            break
    return (returnString)

strs = ["flower","flow","flight"]



longestCommonPrefix(strs)