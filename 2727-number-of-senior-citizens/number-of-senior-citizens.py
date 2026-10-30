class Solution:
    def countSeniors(self, details: List[str]) -> int:
        s=0
        for d in  details:
            if int(d[11:13])>60:
                s+=1
        return s
