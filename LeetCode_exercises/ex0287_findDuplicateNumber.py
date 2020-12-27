"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?

"""



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))

