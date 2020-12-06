"""
    Given two non-negative integers num1 and num2 represented as strings, 
    return the product of num1 and num2, also represented as a string.
    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
    Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"
    Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"

    Constraints:
    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numd = { '0':0 , '1':1 ,'2':2 ,'3':3 ,'4':4 ,'5':5 ,'6':6 ,'7':7 ,'8':8 ,'9':9  }
        if num1=="0" or num2=="0":
            return "0"
        if num1=="1":
            return num2
        if num2=="1":
            return num1
        N1 , N2 = 0, 0
        l = len(num1)-1
        for i in range(len(num1)):
            N1 += numd[num1[i]]*(10**(l-i))
        l=len(num2)-1
        for i in range(len(num2)):
            N2 += numd[num2[i]]*(10**(l-i))
        return str(N1*N2)
