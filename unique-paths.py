class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 for c in range(n)] for r in range(m)]
        
        for r in range(1, m):
            for c in range(1, n):
                memo[r][c] = memo[r-1][c] + memo[r][c-1]

        return memo[m-1][n-1]