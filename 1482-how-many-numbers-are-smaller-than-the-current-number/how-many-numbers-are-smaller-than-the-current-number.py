class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        lst=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if(nums[j]<nums[i]):
                    c+=1
            lst.append(c)
        return lst