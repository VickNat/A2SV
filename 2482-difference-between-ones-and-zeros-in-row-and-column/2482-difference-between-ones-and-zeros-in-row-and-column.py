class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = []
        rowZeroSum = []
        rowOneSum = []
        colZeroSum = []
        colOneSum = []
        gridSize = len(grid)
        colSize = len(grid[0])
        
        for idx in range(gridSize):
            tempZ = 0
            tempO = 0
            
            for elm in range(colSize):
                val = grid[idx][elm]
                
                if val == 0:
                    tempZ += 1
                else:
                    tempO += 1
            
            rowZeroSum.append(tempZ)
            rowOneSum.append(tempO)
        
        for idx in range(colSize):
            tempZ = 0
            tempO = 0
            
            for elm in range(gridSize):
                val = grid[elm][idx]
                
                if val == 0:
                    tempZ += 1
                else:
                    tempO += 1
            
            colZeroSum.append(tempZ)
            colOneSum.append(tempO)
        
        for idx in range(gridSize):
            difference = []

            for elm in range(colSize):
                difference.append((rowOneSum[idx] + colOneSum[elm]) - (rowZeroSum[idx] + colZeroSum[elm]))
                
            diff.append(difference)
        
        return diff
        
        