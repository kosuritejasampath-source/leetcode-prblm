class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid=len(nums)//2
        c=0
        for i in range(len(nums)):
            if(nums[mid]==nums[i]):
                c+=1
        if(c>=2):
            return False
        else:
            return True