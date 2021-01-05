class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col= len(matrix), len(matrix[0])
        change_row, change_col=set(), set()
        
        for i in range(row):
            if 0 not in matrix[i]:
                continue
            change_row.add(i)
            for j in range(col):
                if matrix[i][j]==0:
                    change_col.add(j)
                        
        for i in range(row):
            if i in change_row:
                matrix[i]=[0]*col
            else:
                for j in change_col:
                    matrix[i][j]=0
            
        return
