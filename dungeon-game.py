class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[-float('inf')]*(cols+1) for _ in range(rows+1)]
        
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r == rows-1 and c == cols-1:
                    dp[r][c] = dungeon[r][c]
                else:
                    dp[r][c] = max(dungeon[r][c]+dp[r+1][c], dungeon[r][c]+dp[r][c+1])
                if dp[r][c] > 0:
                    dp[r][c] = 0
        
        return abs(dp[0][0])+1