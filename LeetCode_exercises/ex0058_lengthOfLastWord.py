class Solution:
    # one liner solution
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

class Solution2:
    # intuitive, simple solution
    def lengthOfLastWord(self, s: str) -> int:
        if s==' ':
            return 0

        s = s.split(' ')
        i=len(s)-1
        while i>=0:
            if len(s[i]) != 0:
                return len(s[i])
            else :
                i -= 1 
        return 0
