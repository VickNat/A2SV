class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        max_ = 0

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1

        def dfs(r, c):

            visited.add((r, c))
            counts = 1

            for changeR, changeC in directions:
                newR = r + changeR
                newC = c + changeC

                if inbound(newR, newC) and (newR, newC) not in visited:
                    counts += dfs(newR, newC)
            
            return counts

        for r in range(rows):
            for c in range(cols):
                if inbound(r, c) and (r, c) not in visited:
                    max_ = max(dfs(r, c), max_)
        
        return max_