from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals)
        res=0
        bf=intervals[0]
        for cur in intervals[1:]:
            if cur[0] < bf[1]:
                bf[1]=min(cur[1],bf[1])
                res+=1
            else:
                bf[1]=cur[1]
        return res