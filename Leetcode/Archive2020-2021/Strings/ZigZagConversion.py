"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a
given number of rows like this: (you may want to display this
 pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R



And then read line by line: "PAHNAPLSIIGYIR"


::
On This approach the go up and down approach is applied

Every letter is assigned the row its supposed go to in the order
it appears on the s-string

The rows(keys) and letters(values) are grouped in a  dictionary

The letter(values) are concatenated in the order of the rows  and returned as one String

"""


from collections import defaultdict


def convert(s ,numRows):
    grid = defaultdict()
    row =1
    goingForward = True
    returnString =''
    for i in range(len(s)):
        'I is the index of the letter'
        if row not in grid.keys():
            grid[row] = s[i]
        elif row in grid.keys():
            grid[row] = grid[row]+ s[i]
        if row == 1:
            goingForward = True
        elif row ==numRows:
            goingForward = False

        if goingForward:
            row+=1
        elif not goingForward:
            row-=1
    for key in grid.keys():
        returnString = returnString+ grid[key]

    print(returnString)
    return  returnString







s = "PAYPALISHIRING"

numRows = 3
convert(s ,numRows)
