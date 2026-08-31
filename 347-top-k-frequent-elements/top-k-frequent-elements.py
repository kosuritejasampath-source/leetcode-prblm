class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        values = list(freq.values())
        values.sort()
        result = []
        for i in values[-k:]:
            for j in freq:
                if freq[j] == i:
                    result.append(j)
                    del freq[j]
                    break
        return result