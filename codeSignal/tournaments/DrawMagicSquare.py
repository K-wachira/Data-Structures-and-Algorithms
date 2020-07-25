"""

The drawMagicSquare is a square where we can draw it from its bottom left point and its top right point.
Given two points, bottom left and top right of the square, return the missing top left and bottom right points, where the 4 points can form a square. If the bottom left and top right is not valid or you can't draw a square from the two points , return an empty array.

"""

def drawMagicSquare(bottomLeft, topRight):
    if topRight ==[-1,-1]: return []


    topleft = [topRight[0],bottomLeft[1]]
    bottomRight = [bottomLeft[0],topRight[1]]

    heght , width = 0, 0


    if (topleft[0] - bottomLeft[0] )== (bottomRight[1] - bottomLeft[1]):

        return [topleft,bottomRight]
    return []



bottomLeft = [2, 5]
topRight =[2, 7]

print(drawMagicSquare(bottomLeft,topRight))