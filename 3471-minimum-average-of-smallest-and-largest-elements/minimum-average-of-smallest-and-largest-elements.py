class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        nums.sort()
        i=0
        j=len(nums)-1
        while(i<j):
            m=(nums[i]+nums[j])/2
            avg.append(m)
            i+=1
            j-=1
        return min(avg)