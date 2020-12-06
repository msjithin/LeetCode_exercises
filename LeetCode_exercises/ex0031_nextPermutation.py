"""
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
    The replacement must be in place and use only constant extra memory.

    Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]
    Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]
    Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]
    Example 4:
    Input: nums = [1]
    Output: [1]
    Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100

"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = length -1
        if i==0:
            return 
        # go through the list from end to begining, till a number is greater than the next in line
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        #print('i=', i)
        # if we reach begining of list we return ordered list
        if i <= 0:
            nums.sort()
            return 
        
        # if i > 0, i-1 th element is to be changed, we found the point where we need to change the numbers
        #next find successor to pivot
        j = length - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        #print('nums = ', nums)
        # Reverse suffix
        nums[i : ] = nums[length - 1 : i - 1 : -1]
        return 

