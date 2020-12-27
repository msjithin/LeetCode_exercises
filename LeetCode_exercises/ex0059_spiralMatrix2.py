""" 

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]


"""

class Solution:
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
