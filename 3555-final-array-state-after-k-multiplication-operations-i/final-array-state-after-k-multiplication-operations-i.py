class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        while(k>0):
            m=min(nums)
            for i in range(len(nums)):
                if(m==nums[i]):
                    nums[i]=nums[i]*multiplier
                    break
            k-=1
        return nums