class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pref=[0]*(len(gain)+1)
        for i in range(1,len(gain)+1):
            pref[i]=pref[i-1]+gain[i-1]
        return max(pref)