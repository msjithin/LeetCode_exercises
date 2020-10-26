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
        '''
        1. expand out from a middle letter
        2. stop when 
            a. two letters are not same
            b. edge of string

                  b a b a d
            odd   1 3 3 1 1
            even  0 0 0 0 0
            
                  c b b d
            odd   1 1 1 1 
            even  0 2 0 0
            
            Time O(n^2)
            Space O(1)
        '''
        #return lenght, left index, right index
        if s==s[::-1] or len(s)<=1:
            return s
        def longestAtIndex(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return (r - l + 1, l, r)
        
        longest = 0
        left = 0
        right = -1
        for i in range(len(s)):
            for j in range(2):
                length, l, r = longestAtIndex(s, i, i + j)
                 # j = 0 checks odd palindrome
                 # j=1 checks for even palindrome
                if length > longest: # keep >= if you want last longest palindrome
                    longest = length
                    left = l
                    right = r
        return s[left:right + 1]










