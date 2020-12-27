"""
    Given an unsorted integer array nums, find the smallest missing positive integer.
    Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

    Example 1:

    Input: nums = [1,2,0]
    Output: 3
    Example 2:

    Input: nums = [3,4,-1,1]
    Output: 2
    Example 3:

    Input: nums = [7,8,9,11,12]
    Output: 1
 
    Constraints:
    0 <= nums.length <= 300
   -231 <= nums[i] <= 231 - 1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        nums = [ x for x in sorted(nums) if x>0 ]
        print(nums)
          
        res = 1
        if res not in nums:
            return res
        for n in nums:
            if n+1 not in nums:
                return n+1
        
        return res
