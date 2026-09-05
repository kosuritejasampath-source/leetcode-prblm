class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            max_st=max(nums[:i+1])
            min_st=min(nums[i:])
            diff=max_st-min_st
            if(diff<=k):
                return i
                break
        return -1