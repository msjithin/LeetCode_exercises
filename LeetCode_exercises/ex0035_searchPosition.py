"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:
Input: nums = [1], target = 0
Output: 0
 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0]  > target : return 0
        L = len(nums)
        if nums[-1] < target : return L
        
        res=0
        # bisection search but only one iteration
        left , right = 0, L-1
        mid = (left+right)//2
        if nums[mid] < target :
            res , L = mid , L
        elif nums[mid] > target :
            res , L = 0, mid
        while target > nums[res] and res<L:
            res +=1
            print('while loop : res = ', res)
        return res