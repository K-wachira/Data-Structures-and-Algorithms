"""
Runtime: 36 ms, faster than 36.20% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.6 MB, less than 99.45% of Python3 online submissions for Pascal's Triangle.

https://leetcode.com/problems/pascals-triangle/submissions/
"""



def generate(numRows):
    outputList = [ [1] ]
    z =1

    while z < numRows:
        z+=1
        if (outputList[len(outputList)-1]) == [1]:
            outputList.append([1,1])
        else:
            lastitem = outputList[len(outputList)-1]
            nextItem = [1]
            for i in range(len(lastitem)):
                if i < len(lastitem)-1:
                  nextItem.append(lastitem[i]+lastitem[i+1])
            nextItem.append(1)
            outputList.append(nextItem)
    return outputList

numRows= 54
print(generate(numRows))