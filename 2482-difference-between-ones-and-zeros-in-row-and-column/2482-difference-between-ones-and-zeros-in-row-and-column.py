class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = []
        gridSize = len(grid)
        colSize = len(grid[0])
        rowZeroSum = [0]*gridSize
        rowOneSum = [0]*gridSize
        colZeroSum = [0]*colSize
        colOneSum = [0]*colSize
        
        for idx in range(gridSize):
            for elm in range(colSize):
                val = grid[idx][elm]
                
                if val == 0:
                    rowZeroSum[idx] += 1
                else:
                    rowOneSum[idx] += 1
        
        for idx in range(colSize):
            for elm in range(gridSize):
                val = grid[elm][idx]
                
                if val == 0:
                    colZeroSum[idx] += 1
                else:
                    colOneSum[idx] += 1
        
        for idx in range(gridSize):
            difference = []

            for elm in range(colSize):
                difference.append((rowOneSum[idx] + colOneSum[elm]) - (rowZeroSum[idx] + colZeroSum[elm]))
                
            diff.append(difference)
        
        return diff
        
        
        
        '''
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
        '''
        