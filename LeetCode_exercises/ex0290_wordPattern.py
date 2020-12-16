"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        mymap={}
        
        i=0
        for c in pattern:
            if c not in mymap:
                mymap[c] = s_list[i]
                
            else :
                if s_list[i] != mymap[c]:
                    return False
            i += 1
        #print(mymap)
        tmp = mymap.values()
        if len(tmp) != len(set(tmp)):
            return False
        return True