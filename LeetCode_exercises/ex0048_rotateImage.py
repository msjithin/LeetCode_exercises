"""
    48. Rotate Image

    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to 
    modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output:         [[7,4,1],[8,5,2],[9,6,3]]

    1 2 3      7 4 1
    4 5 6      8 5 2
    7 8 9      9 6 3


"""
from typing import List 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        if length ==1:
            return
        else:
            # first lets reverse
            top , bottom = 0 , length-1
            while top < bottom :
                matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
                top += 1
                bottom -= 1
            # now take transpose :
            for i in range(length):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        