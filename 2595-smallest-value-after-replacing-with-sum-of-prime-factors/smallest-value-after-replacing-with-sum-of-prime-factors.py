class Solution:
    def smallestValue(self, n: int) -> int:
         while True:
            total = 0
            temp = n
            i = 2

            while i <= temp:
                while temp % i == 0:
                    total += i
                    temp //= i

                i += 1

            if total == n:
                return n

            n = total