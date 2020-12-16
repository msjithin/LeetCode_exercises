"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
input  5
output [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res=[]
        if numRows==0:
            return res
        mydict = {   1:[1]
                    ,2:[1,1]
                    ,3:[1,2,1]
                }
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

        for i in range(1, numRows+1):
            addToDict(i)
            #print('checking mydict = ', mydict)
            res.append(mydict[i])
            
        return res

#### for recursive solution use this:

def triangle(n):
    ## need testing
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = triangle(n-1)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
    return new_row










