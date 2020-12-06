"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:
Input: digits = [0]
Output: [1]

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9

"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        L = len(digits)
        tmp=0
        for i in range(L):
            tmp += digits[i] * 10**( L-1-i  )
        tmp += 1
        res = [int(i) for i in str(tmp)]
        zero = 0
        for n in digits :
            if n==0 :
                zero += 1
            else :
                break
        #print(zero)
        while zero > 1:
            res.insert(0,0)
            zero -= 1
        return res
