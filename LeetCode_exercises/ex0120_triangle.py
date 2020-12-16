"""
    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
    For example, given the following triangle
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
    Note:
    Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
class Solution:
    def minimumTotal(self, A) -> int:
        print('A = ')
        for a in A:
            print(a)
        print('\n')
        row = A[-1]
        for i in reversed( range(len(A)-1) ):
            print(i,': row=', row)
            
            for j,x in enumerate(A[i]):
                print('\t j=', j, ' min fn = ', min(row[j],row[j+1]))
                print('\t x = ', x)
            
            row = [ x + min(row[j],row[j+1]) for j,x in enumerate(A[i]) ]
            print('end of loop row=', row)
        print('finally row=', row)    
        return row[0]