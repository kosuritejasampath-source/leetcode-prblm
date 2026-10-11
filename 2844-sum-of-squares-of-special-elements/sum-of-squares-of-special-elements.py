class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        lst=[]
        for i in range(len(nums)):
            if(len(nums)%(i+1)==0):
                lst.append(nums[i])
        s=0
        for i in range(len(lst)):
            s+=lst[i]**2
        return s