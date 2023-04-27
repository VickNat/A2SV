class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        visited.add((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque([[0, 0, 1]])
        N = len(grid)-1

        def inbound(r, c):
            return 0 <= r <= N and 0 <= c <= N and grid[r][c] == 0

        if grid[0][0] == 1:
            return -1

        while queue:
            r, c, path = queue.popleft()
            
            if inbound(r, c) and r == N and c == N:
                return path

            for changeR, changeC in directions:
                newR = r + changeR
                newC = c + changeC

                if inbound(newR, newC) and (newR, newC) not in visited:
                    visited.add((newR, newC))
                    queue.append((newR, newC, path+1))
        
        return -1