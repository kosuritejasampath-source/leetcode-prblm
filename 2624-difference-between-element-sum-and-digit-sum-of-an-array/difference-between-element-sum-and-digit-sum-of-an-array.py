class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        s=sum(nums)
        ds=0
        for i in range(len(nums)):
            n=nums[i]
            while(n>0):
                rem=n%10
                ds+=rem
                n=n//10
        return abs(s-ds)