"""
:: https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.



"""

import numpy as np
def spiralOrder(matrix):
    j = []
    if not matrix: return j
    if len(matrix) == 1:
        j = matrix[0]
    else :
        for i in range(len(matrix)*2):
            try:
                j.extend(matrix[0])
            except IndexError:
                print(matrix)
            matrix = matrix[1:]
            matrix = np.rot90(matrix, 45)
    print(j)
    return (j)










matrix =   [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
            ]

spiralOrder(matrix)