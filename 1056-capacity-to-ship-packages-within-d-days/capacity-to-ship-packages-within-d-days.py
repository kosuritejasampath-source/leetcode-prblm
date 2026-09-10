def canShip(weights,days_have,capacity):
    days_needed=1
    ws=0
    for weight in weights:
        if(ws+weight<=capacity):
            ws+=weight
        else:
            days_needed+=1
            ws=weight
    return days_needed<=days_have
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while(low<high):
            mid=(low+high)//2
            if canShip(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low