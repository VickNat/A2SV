class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = -(heapq.heappop(stones))
            stone2 = -(heapq.heappop(stones))
            stone2 = abs(stone1-stone2)

            if stone2:
                heapq.heappush(stones, -(stone2))

        return abs(stones[0]) if stones else 0