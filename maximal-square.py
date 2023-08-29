class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = defaultdict(int)
        ans = 0

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        def dp(r, c):
            nonlocal ans
            if not inbound(r, c):
                return 0

            if (r, c) in memo:
                return memo[(r, c)]
            
            if matrix[r][c] == "1":
                memo[(r, c)] = 1+min(dp(r+1, c), dp(r, c+1), dp(r+1, c+1))
                ans = max(ans, memo[(r, c)])
            else:
                memo[(r, c)] = min(0, dp(r+1, c), dp(r, c+1), dp(r+1, c+1))
            
            return memo[(r, c)]
        
        dp(0, 0)
        return ans*ans