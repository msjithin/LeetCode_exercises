"""
    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

    Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        num3 = ''
        carry = i = 0
        l1, l2 = len(num1), len(num2)
        l3 = max(l1, l2)
        while i < l3 or carry:
            dig1  = int(num1[i]) if i < l1 else 0
            dig2  = int(num2[i]) if i < l2 else 0
            dig3  = (dig1 + dig2 + carry) % 10
            carry = (dig1 + dig2 + carry) // 10
            num3 = str(dig3) + dig3
            i    += 1
        return num3[::-1]
class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        carry = 0
        idx1 = len(num1)
        idx2 = len(num2)
        while idx1 or idx2 or carry:
            digit = carry 
            if idx1:
                idx1 -= 1
                digit += int(num1[idx1])
            if idx2:
                idx2 -= 1
                digit += int(num2[idx2])
            
            res = str(digit % 10) + res
            carry = digit>=10
        return res