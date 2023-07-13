class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        idx = 0
        size = len(heights)
        heap = []

        for idx in range(size-1):
            diff = heights[idx] - heights[idx+1]
            if diff < 0:
                heappush(heap, -diff)

                if len(heap) > ladders:
                    bricks -= heappop(heap)

                    if bricks < 0:
                        return idx
        
        return size-1