class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alph="abcdefghijklmnopqrstuvwxyz"
        for ch in alph:
            if ch not in sentence:
                return False
        return True