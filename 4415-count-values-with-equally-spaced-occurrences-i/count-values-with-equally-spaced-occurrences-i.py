class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq={}
        k3=[]
        c=0
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key in freq:
            if freq[key]==3:
               k3.append(key)
        for key in k3:
            diff=[]
            for i in range(len(nums)):
                if(nums[i]==key):
                    diff.append(i)
            if(diff[1]-diff[0]==diff[2]-diff[1]):
                c+=1
        return c