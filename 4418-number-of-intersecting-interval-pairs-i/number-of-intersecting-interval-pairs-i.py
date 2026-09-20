class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        c=0
        for i in range(len(intervals)):
            st=intervals[i][0]
            en=intervals[i][1]
            s1=set(range(st,en+1))
            for j in range(i+1,len(intervals)):
                st2=intervals[j][0]
                en2=intervals[j][1]
                s2=set(range(st2,en2+1))
                if s1&s2:
                    c+=1
        return c