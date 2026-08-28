class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid=len(nums)//2
        f=nums[:mid]
        s=nums[mid:]
        lst=[]
        for i in range(n):
            lst.append(f[i])
            lst.append(s[i])
        return lst