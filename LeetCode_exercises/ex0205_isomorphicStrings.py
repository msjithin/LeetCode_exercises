"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""


class Solution:
    """ one liner solution """
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(t))==len(set(zip(s,t)))


class Solution2:
    """ solution with details, mapping """
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mymap = {}
        i = 0
        for i in range(len(s)):
            if s[i] not in mymap:
                mymap[s[i]] = t[i]
            else:
                if t[i] != mymap[s[i]]:
                    return False
        if len(set(t)) != len(set(s)):
            return False
        return True