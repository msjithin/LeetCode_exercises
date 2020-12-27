"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # first sort the list of intervals
        # for loop the intervals, and merge if needed
        intervals.sort(key = lambda x : x[0])        
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            last_start, last_end = res[-1]
            cur_start, cur_end = intervals[i]
            if last_end < cur_start: res.append(intervals[i])
            elif cur_start <= last_end and last_end <= cur_end: res[-1][1] = cur_end
            elif cur_start <= last_end and cur_end <= last_end: continue
                
        return res
