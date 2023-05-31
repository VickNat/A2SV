class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        memo[(0,0)] = 1


        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        def dp(cell):
            if cell in memo:
                return memo[cell]
            
            up = (cell[0]-1, cell[1])
            down = (cell[0], cell[1]-1)

            val = 0
            if inbound(up[0], up[1]):
                val += dp(up)
            if inbound(down[0], up[1]):
                val += dp(down)

            memo[cell] = val
            return memo[cell]
    
        dp((m-1, n-1))
        return memo[(m-1, n-1)]