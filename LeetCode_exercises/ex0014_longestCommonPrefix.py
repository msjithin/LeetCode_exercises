"""
    14. Longest Common Prefix
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=''
        numStrings=len(strs)
        if numStrings==0  or len(strs[0])==0:
            return ''
        if numStrings==1:
            return ''.join(strs)
        counter=0
        length=0
        foundPrefix=True
        while foundPrefix and length<len(strs[0]) :
            counter=0
            elementToCheck=strs[0][length]
            for i in range( 1, len(strs)  ):
                if len(strs[i])==0:
                    return ''
                if length<len(strs[i]) and elementToCheck == strs[i][length] :
                    counter+=1
            if counter==len(strs)-1:
                foundPrefix=True
                length+=1
            else:
                foundPrefix=False
        result += strs[0][:length]
        return result


    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        if not strs:return ''
        a,b = min(strs),max(strs) # min max is selected based on letter's place in albhabets
        print('a', a, 'b', b)
        for i in range(len(a)):
            print(a[i], b[i])
            if a[i]!= b[i]:
                return a[:i]
        return a
    def longestCommonPrefix_3(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort() # sorted based on letter's place in albhabets
        print(strs)
        prefix1 = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                prefix1 +=x
            else:
                break
        return prefix1
            
