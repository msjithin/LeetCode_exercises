"""
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment that could only
store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""
class Solution:
    def reverse(self, x: int) -> int:
        str_out=''
        if x>=0:
            str_in=str(x)
        else:
            str_in=str(x)[1:]
        for i in range(len(str_in)-1, -1,-1):
            str_out+=str_in[i]
        if not len(str_out) >0 :
            return 0
        rev_int = int(str_out)
        if(rev_int>2147483647 or rev_int<-2147483648):
            return 0
        if(x<0):
            return rev_int*-1
        elif(x>0):
            return rev_int
        elif(x==0):
            return 0

    def reverse_fn2(self, x: int) -> int:
        '''
        This is faster and more refined
        '''
        def reverseit(x):
            return int(str(abs(x))[::-1])

        def checkint(x):
            if((x < -2**31) or (x > 2**31)):
                return 0
            else:
                return x

        if (x < 0):
            return checkint((-1)*reverseit(x))

        else:
            return checkint(reverseit(x))