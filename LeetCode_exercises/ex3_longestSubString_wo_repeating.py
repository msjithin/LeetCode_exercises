'''
Given a string s, find the 
length of the longest substring
without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter=0
        previousLetter=''
        max_counted=0
        for letter in s:
            #print('letter in string: '+letter)
            #print(letter+' '+previousLetter+" "+str(counter))
            if letter in previousLetter:
                prIndex=previousLetter.index(letter)
                counter=len(previousLetter)-(prIndex )
                previousLetter+=letter
                previousLetter=previousLetter[prIndex+1:]
                #print('letter found : '+previousLetter)

            else:
                previousLetter+=letter
                counter+=1
            if counter > max_counted:
                max_counted=counter
        print(previousLetter+' '+str(max_counted))
        return max_counted