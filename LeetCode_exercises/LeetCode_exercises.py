

import ex5_longestPalindromicSubstring as ex5

ex5sln = ex5.Solution()
input_strings=['babad', 'cbbd', 'a', 'ac', 'xabax', 'xabay', 'ccc', 'abb','aacabdkacaa']
for s in input_strings:
    print('input string='+s+ '  output :'+ ex5sln.longestPalindrome(s)   )