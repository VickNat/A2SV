class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        prefixRow1 = [0]*(cols+1)
        prefixRow2 = [0]*(cols+1)

        for idx in range(1, cols+1):
            prefixRow1[idx] = prefixRow1[idx-1] + grid[0][idx-1]
            prefixRow2[idx] = prefixRow2[idx-1] + grid[1][idx-1]
        
        res = float('inf')

        for idx in range(1, cols+1):
            top = prefixRow1[-1] - prefixRow1[idx]
            bottom = prefixRow2[idx-1]

            secondRobot = max(top, bottom)
            res = min(secondRobot, res)
        
        return res