class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonalMat = []
        cols = len(mat[0])
        rows = len(mat)
        col = 0
        row = 0
        idx = 0
        
        while idx <= rows*cols and row < rows:
            if (row + col)%2 == 0:
                while row >= 0 and col < cols:
                    diagonalMat.append(mat[row][col])
                    
                    row -= 1
                    col += 1
                
#                 to take row back in range of rows
                row += 1
                
#                 in the case that col is out of range
                if col >= cols:
                    col -= 1
                    row += 1
                
            elif (row + col)%2 != 0:
                while col >= 0 and row < rows:
                    diagonalMat.append(mat[row][col])
                    
                    row += 1
                    col -= 1
                
                col += 1
                
#                 Same case as the rows situation
                if row >= rows:
                    row -= 1
                    col += 1
            
#             update the main iteration
            idx += 1
            
        return diagonalMat