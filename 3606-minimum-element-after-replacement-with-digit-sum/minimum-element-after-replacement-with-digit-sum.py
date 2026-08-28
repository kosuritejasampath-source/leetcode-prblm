class Solution:
    def minElement(self, nums: List[int]) -> int:
        def s(n):
            s=0
            while(n>0):
              temp=n%10
              s+=temp
              n=n//10
            return s  
        lst=[]
        for i in range(len(nums)):
            lst.append(s(nums[i]))
        return min(lst)