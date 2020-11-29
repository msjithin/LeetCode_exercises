"""
38. Count and Say
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
which is then converted into a different digit string.
To determine how you "say" a digit string, 
split it into the minimal number of groups so that each group is a contiguous section all of the same character. 
Then for each group, say the number of characters, 
then say the character. To convert the saying into a digit string, 
replace the counts with a number and concatenate every saying.

"""
class Solution:
    d = {1:'1',2:'11',3:'21',4:'1211'}
    def getString(self, n: str) -> str:
        res = ''
        count,cur = 1,n[0]
        for i in range(1,len(n)):
            if n[i] == cur:
                count += 1
            else:
                res += str(count) + cur
                cur = n[i]
                count = 1
        res += str(count) + cur
        return res
    def countAndSay(self, n: int) -> str:    
        rvstr=""
        if n not in self.d:
            previous = self.countAndSay(n-1)
            self.d[n] = self.getString(previous)
        return self.d[n]


class Solution2:
    d = {1:'1',2:'11',3:'21',4:'1211'}    
    def countAndSay(self, n: int) -> str:    
        rvstr=""
        if n not in self.d:
            previous = self.countAndSay(n-1)
            tmp=[]
            count=[]
            for num in previous:
                if len(tmp)==0 or num != tmp[-1] :
                    tmp.append(num)
                    count.append(1)
                else:
                    count[-1]+=1

            for i in range(len(tmp)):
                rvstr+=str(count[i]) + str(tmp[i])
            self.d[n] = rvstr
        return self.d[n]

