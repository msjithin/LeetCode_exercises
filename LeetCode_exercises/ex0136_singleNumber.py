"""
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""
from typing import List
from numpy import inf

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ best solution I found, quite short """
        return 2 * sum(set(nums))-sum(nums)

class Solution:
    """ understand this"""
    def singleNumber(self, nums: List[int]) -> int:
        i=0
        for j in nums:
            i=i^j
        return i
        
class Solution:
    """ try removinf elements if second copy is present"""
    def singleNumber(self, nums: List[int]) -> int:
        i=1
        while i<len(nums):
            try:
                x=nums[i]
                if x in nums[0:i]:
                    nums.remove(x)
                    nums.remove(x)
                    i-=1
                else:
                    i+=1
            except IndexError:
                break
        return nums[0]