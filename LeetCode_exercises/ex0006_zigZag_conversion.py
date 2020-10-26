class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        """
        Approach 1 : 
        Time: O( n+k < n+n <2n ) = O(n)
        Space: O(n)
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>=len(s):
            return s
        delta=-1
        row=0
        res=[[] for i in range(numRows)]
        
        for c in s:
            res[row].append(c)
            if row==0 or row== numRows-1:
                delta *= -1
            row += delta
            
        for i in range(len(res)):
            res[i]= ''.join(res[i])
        return ''.join(res)
    def convert2(self, s: str, numRows: int) -> str:
        """
        Approach 2 :
        if numRows=4
        row 0 ==>  0 6 12 ...   0 +6 +6
        row 1 ==>  1 5 7 13 ... 1 +4 +2 +4
        row 2 ==>  2 4 8 10 ... 2 +2 +4 +2
        row 3 ==>  3 9 ....     3 +6 +6

        if numRows=3
        row 0 ==>  0 4 8 ...   0 +4 +4
        row 1 ==>  1 3 5 7...  1 +2 +2 
        row 2 ==>  2 6 10...   2 +4 +4

        cycle:  ==> 2*numRows - 2
        1 -> 1 special case
        2 -> 2 
        3 -> 4
        4 -> 6
        

        Time: O(n) = O(n)
        Space: O(n)
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        cycle = 2*numRows - 2
        res=[]
        for i in range(numRows):
            for j in range(i, len(s), cycle):
                res.append(s[j])
                k = j+cycle -2*i
                if i!=0 and i != numRows-1 and k<len(s):
                    res.append(s[k])
        return ''.join(res)

