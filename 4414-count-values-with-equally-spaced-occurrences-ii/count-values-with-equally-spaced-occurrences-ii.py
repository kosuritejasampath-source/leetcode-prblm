class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq={}
        pos={}
        c=0
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
                pos[nums[i]].append(i)
            else:
                freq[nums[i]]=1
                pos[nums[i]]=[i]
        for key in freq:
            if(freq[key]>=3):
                diff=pos[key]
                d=diff[1]-diff[0]
                spcl=True
                for i in range(2,len(diff)):
                    if(diff[i]-diff[i-1]!=d):
                        spcl=False
                        break
                if spcl:
                    c+=1
        return c
            