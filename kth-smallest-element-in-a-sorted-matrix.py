class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        counts = 0
        cur = 0

        for i in range(n):
            heappush(heap, (matrix[i][0], (i, 0)))
            
        while counts < k:
            cur, (r, c) = heappop(heap)
            counts += 1

            if c+1 < n:
                heappush(heap, (matrix[r][c+1], (r, c+1)))

        return cur