class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        while low <= high:
            mid=low+(high-low)//2
            hours_spent=0
            for pile in piles:
                hours_spent+=math.ceil(pile/mid)
            if hours_spent<=h:
                high=mid-1
            else:
                low=mid+1
        return low
        