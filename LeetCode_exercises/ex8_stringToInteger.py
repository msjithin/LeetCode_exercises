'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters 
as necessary until the first non-whitespace character is found. 
Then, starting from this character takes an optional 
initial plus or minus sign followed by 
as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those 
that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in 
str is not a valid integral number, or if no such sequence exists 
because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.
Note:
Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store 
integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: str = "42"
Output: 42

Example 2:
Input: str = "   -42"
Output: -42

Example 3:
Input: str = "4193 with words"
Output: 4193

Example 4:
Input: str = "words and 987"
Output: 0

Example 5:
Input: str = "-91283472332"
Output: -2147483648
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        in_string = s.strip()
        if len(in_string)==0 :
            return 0
        returnString=''
        MAX_INT = 2**31 -1
        MIN_INT = -1*(2**31)
        def checkSign(charFound):
            if charFound in '-':
                return -1
            elif charFound in '+':
                return 1
            return 1
        def checkRange(num):
            if num > MAX_INT :
                return MAX_INT
            if num < MIN_INT :
                return MIN_INT
            return num

        signFromString=checkSign(in_string[0])
        if in_string[0] in '+-':
            in_string = in_string[1:]
        for character in in_string:
            if character.isnumeric():
                returnString+=character
            else:
                break
        if len(returnString)==0:
            return 0
        return checkRange( signFromString*int(returnString)  )




