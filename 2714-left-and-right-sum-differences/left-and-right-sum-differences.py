class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls=[0]*len(nums)
        rs=[]
        for i in range(1,len(nums)):
            ls[i]=ls[i-1]+nums[i-1]
        s=sum(nums)
        for i in range(len(nums)):
            s-=nums[i]
            rs.append(s)
        lst=[]
        for i in range(len(ls)):
            lst.append(abs(ls[i]-rs[i]))
        return lst