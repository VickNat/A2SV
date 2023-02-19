class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        r = n-2
        c = n-2
        ans = [[0]*r for _ in range(c)]
        offRow = 0
                
        while offRow + 3 <= n:
            offCol = 0
            
            while offCol + 3 <= n:
                maxVal = 0

                for idx in range(offRow, offRow + 3):
                    maxCol = max(grid[idx][offCol:offCol + 3])
                    maxVal = max(maxVal, maxCol)
                
                ans[offRow][offCol] = maxVal
                offCol += 1
                
            offRow += 1
        
        return ans
        
        