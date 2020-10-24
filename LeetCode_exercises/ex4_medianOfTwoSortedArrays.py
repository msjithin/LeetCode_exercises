from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        outlist=[]
        outlist = nums1+nums2
        outlist = sorted(outlist)
        print(outlist)
        length = len(outlist)
        midindex=int(length/2)
        median = 0
        print( 'lenght:', length, 'midindex:', midindex   ) 
        if length==0:
            median=0
        elif length==1:
            median= outlist[0]
        elif length%2==0:
            median= ( outlist[midindex-1] + outlist[midindex] )/2
        else:
            median= outlist[midindex]
        
        return float(median)





