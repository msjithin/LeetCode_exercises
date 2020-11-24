"""
    Given an array nums of n integers, are there elements a, b, c in nums 
    such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    Notice that the solution set must not contain duplicate triplets.

    Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Example 2:
    Input: nums = []
    Output: []
    Example 3:
    Input: nums = [0]
    Output: []
 
    Constraints:
    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""
from typing import List
from collections import defaultdict



class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum( nums, s) -> List[List[int]]:
            d = set()
            result = []
            for n in nums:
                #print(n, d)
                if s-n in d:
                    result.append([s-n, n])
                d.add(n)
                #print(d)
            return result
        nums.sort()
        result_set = set()
        result = []
        i = 0 
        while i < len(nums) and nums[i] <= 0:
            n = nums[i]
            two_sum_results = twoSum(nums[i+1:], -n)
            if two_sum_results:
                for r in two_sum_results:
                    triplet = r + [n]
                    triplet.sort()
                    triplet_tuple = tuple(triplet)
                    #print('triplet_tuple',triplet_tuple)
                    if triplet_tuple not in result_set:
                        result_set.add(triplet_tuple)
                        result.append(triplet)
                    #print('result_set', result_set)
            i+=1
            while i < len(nums) and nums[i] == nums[i-1]:
                i+=1
        return result
                
    
