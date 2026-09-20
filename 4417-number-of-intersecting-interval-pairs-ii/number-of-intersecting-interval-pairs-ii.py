from bisect import bisect_left
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        starts=[]
        ends=[]
        for start,end in intervals:
            starts.append(start)
            ends.append(end)
        starts.sort()
        ends.sort()
        c=0
        for i in range(len(starts)):
            not_intersect=bisect_left(ends,starts[i])
            c+=i-not_intersect
        return c