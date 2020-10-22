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
#class Solution:
#    def longestPalindrome(self, s: str) -> str:
#        return ''
#s = 'babad'

#def checkIfPalindrome(stringtocheck):
#   if stringtocheck == stringtocheck[ ::-1 ]:
#       return True
#   return False
            
    
#def cheackForPalindrome(s):
#    currentString=s
#    lengthOfString = len(currentString)
#    palindrome = ''
#    for i, letter in enumerate(currentString):
#        palindrome=letter
#        if checkIfPalindrome(palindrome):
#            palindrome = currentString[i-1] + letter + currentString[i+1]