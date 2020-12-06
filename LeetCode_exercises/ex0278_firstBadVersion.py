"""
278. First Bad Version
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
 
Constraints:
1 <= bad <= n <= 231 - 1
"""

class Solution:
    def __init__(self, n, firstbad):
        self.n=n
        self.firstbad=firstbad

    def isBadVersion(self, k):
        if k < self.firstbad:
            return False
        else:
            return True

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        if isBadVersion(1)==True: return 1
        left, right  = 1, n
        mid = (left+right)//2
        
        while left < right :
            
            if isBadVersion(mid)==False :
                left = mid
            elif isBadVersion(mid)==True :
                right = mid+1
            
            mid = (left+right)//2
            if isBadVersion(mid)==True and isBadVersion(mid-1)==False :
                break
            if isBadVersion(right)==True and isBadVersion(right-1)==False :
                mid = right
                break
        return mid

    def firstBadVersion_v2(self, n):  # this is a shorter,cleaner version
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        if isBadVersion(1)==True: return 1
        left, right  = 1, n
        l = 1
        r = n
        while (l < r):
            m = l + (r-l)/2
            if (isBadVersion(m) == True):
                r = m
            else:
                l = m + 1
        return int(l)
