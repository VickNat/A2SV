class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        counts = 0
        
        for idx in range(len(piles)):
            piles[idx] = -piles[idx]
        
        heapify(piles)

        while counts < k:
            val = -(heappop(piles))
            minus = val//2
            heappush(piles, -(val-minus))
            counts += 1
        
        return -(sum(piles))