class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        for i in nums1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        result = []
        for i in nums2:
            if i in freq and freq[i] > 0:
                result.append(i)
                freq[i] -= 1
        return result