"""
TWO SUM 

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
in_list=[2,7,11,15]
target = 9
print(
    two_sum.twoSum(in_list, target)
      )
"""
from typing import List


class Class_twoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            n=target - num
            #print(i, num, seen)
            if n not in seen:
                seen[num] = i
            else:
                return [seen[n], i]

    def my_fn(self, nums:List[int], target:int)-> List[int]:
        for i in nums :
            n=target-i
            if n in nums:
                return [nums.index(i), nums.index(n)]
        return []
