class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        size = len(piles)
        piles.sort()
        left = 0
        right = piles[-1]+1
        
        while left+1 < right:
            mid = left+(right-left)//2
            hours = 0

            for elm in piles:
                hours += ceil(elm/mid)
        
            if hours <= h:
                right = mid
            elif hours > h:
                left = mid

        return right