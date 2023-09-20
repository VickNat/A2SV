class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = defaultdict(int)
        directions = [(-1, 0), (-1, 1), (-1, -1)]

        def dp(r, c):
            if r == 0:
                memo[(r, c)] = matrix[r][c]
                return memo[(r, c)]
            
            if (r, c) in memo:
                return memo[(r, c)]

            min_ = float('inf')
            for changeR, changeC in directions:
                newR = r+changeR
                newC = c+changeC

                if newC >= 0 and newC < rows:
                    min_ = min(dp(newR, newC)+matrix[r][c], min_)
            
            memo[(r, c)] = min_
            return min_
        
        ans = float('inf')
        for c in range(cols):
            ans = min(ans, dp(rows-1, c))

        return ans