class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        subIslands = 0

        def inbound(r, c):
            return (0 <= r < rows) and (0 <= c < cols)
        
        def dfs(r, c):

            visited.add((r, c))
            ans = True

            for changeR, changeC in directions:
                newR = r + changeR
                newC = c + changeC

                if inbound(newR, newC) and grid2[newR][newC] == 1 and (newR, newC) not in visited:
                    ans &= dfs(newR, newC)
            
            if ans and grid1[r][c] == 1:
                return True
            return False
        
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and (r, c) not in visited:
                    if dfs(r, c):
                        subIslands += 1

        return subIslands