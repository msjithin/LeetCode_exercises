"""
    Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
    Notice that the row index starts from 0.
    Could you optimize your algorithm to use only O(k) extra space?
"""
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # recursive solution
        if rowIndex == 0:
            return [1]
        lastRow = self.getRow(rowIndex - 1)
        res = [1]
        for i in range(len(lastRow) - 1):
            res.append(lastRow[i] + lastRow[i + 1])
        res.append(1)
        return res

    def getRow2(self, rowIndex: int) -> List[int]:
        
        mydict = { 0:[1], 1:[1,1]  }
        if rowIndex in mydict:
            return mydict[rowIndex]
        
        def addToDict(n):
            if n in mydict:
                return
            else:
                tmp=[]
                tmp.append(1)
                i=0
                previous = mydict[n-1]
                while i+1 < n-1:
                    tmp.append( previous[i]+previous[i+1]  )
                    i += 1
                tmp.append(1)
                #print('tmp=', tmp)
                mydict[n] = tmp
                return

        for i in range(1, rowIndex+2):
            addToDict(i)
            #print('checking mydict = ', mydict)
            
            
        return mydict[rowIndex+1]