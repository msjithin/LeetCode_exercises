class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag = len(nums)-1
        for i in range(flag,-1,-1):
            if nums[i]+i >= flag:
                flag = i
        return flag == 0
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        made_it = False
        target = 0
        for i in range(1,len(nums)):
            idx = len(nums) - 1 - i 
            if nums[idx] >= i - target:
                target = i
                
        return target == len(nums)-1

class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        made_it = False
        target = 0
        for i in range(1,len(nums)):
            idx = len(nums) - 1 - i 
            if nums[idx] >= i - target:
                target = i
                
        return target == len(nums)-1