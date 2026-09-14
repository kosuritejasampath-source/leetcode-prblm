class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        if k > 0:
            window_sum = 0
            for i in range(1,k+1):
                window_sum += code[i%n]
            for i in range(n):
                ans[i] = window_sum
                window_sum -= code[(i+1)%n]
                window_sum += code[(i+k+1)%n]
        else:
            k = -k
            window_sum = 0
            for i in range(1,k+1):
                window_sum += code[(n-i)%n]
            for i in range(n):
                ans[i] = window_sum
                window_sum -= code[(i-k)%n]
                window_sum += code[i]
        return ans