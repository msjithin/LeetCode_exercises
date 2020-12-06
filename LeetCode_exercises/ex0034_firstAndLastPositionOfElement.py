"""
    34. Find First and Last Position of Element in Sorted Array
    Given an array of integers nums sorted in ascending order, 
    find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    Follow up: Could you write an algorithm with O(log n) runtime complexity?

    Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
    Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]

    Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        finalId = len(nums)-1
        if finalId<0:
            return [-1,-1]
        if nums[0]==target and nums[finalId]==target:
            return [0, finalId]
        # lets try bisection search
        left, right = 0, finalId
        counter=0
        mid = (left+right)//2
        while left <= right  :
            counter+=1
            if counter == len(nums):
                print('something is wrong .............................')
                break
            mid = (left+right)//2
            print('index   left {} , right {} , mid {} '.format(left, right, mid))
            print('values  left {} , right {} , mid {} '.format(nums[left], nums[right], nums[mid]))

            if nums[mid] > target :
                left, right = left , mid-1
            elif nums[mid] < target :
                left, right = mid+1 , right
            elif nums[mid]==target :
                break
        
        if mid==0 and nums[left]==target:
            mid=left
        if mid==0 and nums[right]==target:
            mid=right
        print('final I  left {} , right {} , mid {} '.format(left, right, mid))
        print('final V  left {} , right {} , mid {} '.format(nums[left], nums[right], nums[mid]))
        if nums[mid] != target :
            return [-1, -1]
        else :
            left, right = mid, mid
        while left >=1:
            if nums[left-1]==target :
                left-=1
                break
            else:
                break
        while right < finalId:
            if nums[right+1]==target:
                right+=1
                break
            else:
                break

        return [left, right]





class Solution2:
    # brute force method
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        finalId = len(nums)-1
        if finalId<0:
            return [-1,-1]
        if nums[0]==target and nums[finalId]==target:
            return [0, finalId]

        tmp=[]
        for i in range(len(nums)):
            if nums[i]==target:
                tmp.append(i)
            elif nums[i] > target:
                break
        print(tmp)
        
        if len(tmp)>0 :
            return [tmp[0], tmp[-1]] 
        else :
            return [-1, -1]