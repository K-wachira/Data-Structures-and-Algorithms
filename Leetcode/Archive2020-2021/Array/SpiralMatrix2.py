"""
:: https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

"""

def spiralOrder(matrix):

    j =[]

    if not matrix: return j
    wallNumber = 1

    for i in range(len(matrix)*2):
        if wallNumber == 1:
            j.extend(matrix[0])
            matrix = matrix[1:]
        elif wallNumber == 2:
            for i in matrix:
                j.append(i[len(i)-1])
                i.remove(i[len(i)-1])
        elif wallNumber == 3:
            j.extend(matrix[len(matrix)-1][::-1])
            matrix= matrix[:len(matrix)-1]
        else:
            try:
             if len(matrix[0]) > 0 and wallNumber == 4:
                for i in matrix[::-1]:
                    j.append(i[0])
                    i.remove(i[0])
            except IndexError:
                print("")
        if wallNumber < 4:
            wallNumber+=1
        else:
            wallNumber=1



    print(j)
    return j








matrix =[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]


spiralOrder(matrix)

[1,2,3,4,8,12,16,15,14,13,5,9,6,7,11,10]
[1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

