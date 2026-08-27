class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq={}
        def prime(n):
            if(n<2):
                return False
            for i in range(2,int(n**0.5)+1):
                if(n%i==0):
                    return False
            return True
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for value in freq.values():
            if prime(value):
                return True
        return False