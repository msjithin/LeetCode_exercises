"""
    Given a string containing just the characters '(' and ')', 
    find the length of the longest valid (well-formed) parentheses substring.

    Example 1:
    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".
    Example 2:
    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".
    Example 3:
    Input: s = ""
    Output: 0
 
    Constraints:
    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.
"""

"""
test samples 
"()(()" -> 4
"())"   -> 2
")("    -> 0
"()()" -> 4
"()(())" -> 6

"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res, leftmost = 0, -1
        stack = []
        for i in range(len(s)):
            #print('i=', i, 'element=', s[i])
            #print(' stack = ', stack)
            #print('     leftmost = ', leftmost , "res=", res)
            if s[i] == '(':
                stack.append(i)
            else: #c == ')'
                if not stack:
                    leftmost = i
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i-leftmost)
                    else:
                        res = max(res, i-stack[-1])
        return res
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        #s=list(s)
        Length = len(s)
        if Length==1:
            return 0
        if s=='()':
            return 2        
        #if s[0]=='(' and s[-1]==')':
        #    return Length
        def checkbraket(start, end):
            #res=[]
            tmp=-99
            for i in range(end):
                # pick a (
                if s[i] =='(' :
                    for j in range(i+1, end):
                        # pick a )
                        if s[j]==')' :
                            #res.append([i,j])
                            if tmp< j-i :
                                tmp= j-i
            #print(res)
            return tmp
        res=0
        for index in range(Length):
            res=checkbraket(index, Length)
            #print(res)
        return res if res>0 else 0
