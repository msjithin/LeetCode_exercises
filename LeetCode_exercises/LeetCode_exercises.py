

import ex0032_longestValidParanthesis as ex32

s = {   
    "(()" : 2 ,
    ")()())" : 4,
    "" : 0,
    "()(()" :  4,
    "())"   : 2,   
    ")("    : 0,
    "()()"  : 4,
    "()(())"  :  6
    }

for b in s :
    print('input string = {} ,\t expected={} ,\t output={}  '.format(b, s.get(b), ex32.Solution().longestValidParentheses(b) ))
    #print('testing solution : {} \n\n'.format(ex32.Solution2().longestValidParentheses(b)))