class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime=[True]*(right+1)
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,int(right**0.5)+1,1):
            if is_prime[i]:
                for j in range(i*i,right+1,i):
                    is_prime[j]=False
        prev=-1
        ans=[-1,-1]
        min_gap=100000000
        for num in range(left,right+1):
            if is_prime[num]:
                if prev!=-1:
                    gap=num-prev
                    if(gap<min_gap):
                        min_gap=gap
                        ans=[prev,num]
                prev=num
        return ans