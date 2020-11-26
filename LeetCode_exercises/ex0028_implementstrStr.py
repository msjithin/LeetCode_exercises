"""
    Implement strStr().
    Return the index of the first occurrence of needle in haystack, 
    or -1 if needle is not part of haystack.
    Clarification:
    What should we return when needle is an empty string? 
    This is a great question to ask during an interview.
    For the purpose of this problem, we will return 0 when needle is an empty string. 
    This is consistent to C's strstr() and Java's indexOf().

    Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0

        if needle not in haystack:
            return -1
        for i in range(len(haystack)-(len(needle)-1)): # we need not go the last len(needle)-1 chars
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
            
