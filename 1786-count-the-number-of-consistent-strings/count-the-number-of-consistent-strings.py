class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
         c=0
         for word in words:
            flag=True
            for ch in word:
                if ch not in allowed:
                    flag=False
                    break
            if flag:
                c+=1
         return c