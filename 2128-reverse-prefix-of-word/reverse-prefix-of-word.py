class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans=0
        for i in range(len(word)):
            if word[i]==ch:
                ans=i
                break
        return word[:ans+1][::-1]+word[ans+1:]