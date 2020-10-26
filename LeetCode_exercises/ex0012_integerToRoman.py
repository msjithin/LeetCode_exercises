"""
    Integer to Roman
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two one's added together. 
    12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. 
    However, the numeral for four is not IIII. Instead, the number four is written as IV. 
    Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. 
    There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral.
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        The roman numeral for 2513 is MMDXIII.
        That is because 2513 = 2000 (MM) + 500 (D) + 10 (X) + 3(III)
        So the question is, how can we split 2513 into 2000, 500, 10 and 3?
        We can use division and modulus (remainder).
        int(2513/1000) gives us 2. This tells us that there are two ‘1000’s, which translates to ‘MM’.
        2513%1000 gives us 513. This removes 2000 from the original number.
        We can repeat the two steps above until the entire number is converted. This happens when the remainder is 0.
        In other words, the steps for converting 2513 are:
        int(2513/1000) = 2
        result = 'MM'
        2513%1000 = 513

        int(513/500) = 1
        result = 'MMD'
        513%500 = 13

        int(13/10) = 1
        result = 'MMDX'
        13%10 = 3

        int(3/1) = 3
        result = 'MMDXIII'
        3%1 = 0
                '''
        result = ''
        mapping = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        if num in mapping:
            return mapping[num]
        while num != 0:
            for key, value in mapping.items():
                if num >= key:
                    dividend = int(num/key)
                    num %= key
                    result += dividend*value
        return result
