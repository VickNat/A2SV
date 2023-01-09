class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counts = 0
        compare = []
        gridSize = len(grid)
        rowSize = len(grid[0])
        
        for colIdx in range(rowSize):
            temp = []
            
            for col in range(gridSize):
                temp.append(grid[col][colIdx])
            
            compare.append(temp)
        
        for gridRow in range(gridSize):
            for cmpRow in range(len(compare)):
                gridComp = grid[gridRow]
                cmpComp = compare[cmpRow]
                
                if gridComp == cmpComp:
                    counts+=1
        
        return counts
    
    
    
#         for row in range(gridSize):
#             checkRow = grid[row]
            
#             if checkRow not in checkDict.keys():
#                 checkDict[checkRow] = 0
#             elif checkRow in checkDict.keys():
#                 checkDict[checkRow] += 1