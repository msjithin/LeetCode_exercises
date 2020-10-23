"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
1) 1 <= s.length <= 1000
2) s consist of only digits and English letters (lower-case and/or upper-case),
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        start = 0
        for i in range(1,len(s)):
            # consider adding 2
            if i-max_length-1 >= 0:
                if s[i-max_length-1:i+1] == s[i-max_length-1:i+1][::-1]:
                    start = i-max_length-1
                    max_length += 2
                    
            if i-max_length >= 0:
                if s[i-max_length:i+1] == s[i-max_length:i+1][::-1]:
                    print(s[i-max_length:i+1],s[i-max_length:i+1][::-1])
                    print(s[i-max_length:i+1]==s[i-max_length:i+1][::-1])
                    start = i-max_length
                    max_length += 1
                    #print("start",start)
        
        return s[start:start+max_length]
