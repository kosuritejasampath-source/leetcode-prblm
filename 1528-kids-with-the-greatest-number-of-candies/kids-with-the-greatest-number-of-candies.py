class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        s=0
        lst=[]
        m=max(candies)
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=m):
                lst.append(True)
            else:
                lst.append(False)
        return lst