class Solution:
    def pivotInteger(self, n: int) -> int:
        pref=[0]*(n+1)
        for i in range(1,n+1):
            pref[i]=pref[i-1]+i
        total=pref[n]
        for i in range(1,n+1):
            left=pref[i]
            right=total-pref[i-1]
            if(left==right):
                return i
        return -1