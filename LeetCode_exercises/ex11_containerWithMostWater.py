"""
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i 
is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, 
such that the container contains the most water.
Notice that you may not slant the container.
"""
from typing import List
class Solution:
    def maxArea1(self, height: List[int]) -> int:
        '''
        This is brute force
        Time O(n^2)
        Space O(1)
        NOT good for long lists
        '''
        bestArea=0
        for i in range(len(height)):
            for j in range(i+1, len(height) ):
                bestArea = max( bestArea , min(height[i], height[j])*(j-i) )
        return bestArea

    def maxArea(self, height: List[int]) -> int:
        '''
        Optimal solution
        [1,8,6,2,5,4,8,3,7]
                h  w
        1, 7==> 1  8 --> 8
        1, 3==> 1  7 --> 7
        1, 8==> 1  6 --> 6
        best width == first thing we check, farthest away
        best height == smaller height

        ==> assuming we check the smaller height, fartest one gives max area

        8, 7 ==> 7 7 --> 49
        6, 7 ==> 6 
        2, 7 ==> 2
        algorith:
        1. check left and right most height
        2. calculate local cara
        3. move in from lower height

        Time O(n)
        Space O(1)

        '''
        bestArea = 0
        left = 0
        right = len(height)-1
        while left < right:
            #print('left', left, 'right', right)
            #print('left h', height[left], 'right h', height[right])
            bestArea = max( bestArea , min(height[left], height[right])*(right-left) )
            #print('best area = ', bestArea)
            if height[left]<height[right]:
                left+=1
            else:
                right -=1

        return bestArea