class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        size = rows*cols
        spiral = []
        counts = 0
        
#         Declare the 4 pointers
        lRow = -1
        lCol = -1
        rCol = cols
        rRow = rows
        
        row = 0
        col = 0
        
        while counts < size:
            lRow += 1
            while col != rCol:
                spiral.append(matrix[row][col])
                col += 1
                counts += 1
            
            if counts >= size:
                break
                
            rCol -= 1
            col -= 1
            row += 1
            
            while row != rRow:
                spiral.append(matrix[row][col])
                row += 1
                counts += 1
            
            if counts >= size:
                break
            
            rRow -= 1
            row -= 1
            col -= 1
            
            while col != lCol:
                spiral.append(matrix[row][col])
                col -= 1
                counts += 1
            
            if counts >= size:
                break
            
            col += 1
            lCol += 1
            row -= 1
            
            while row != lRow:
                spiral.append(matrix[row][col])
                row -= 1
                counts += 1
            
            row += 1
            col += 1

        return spiral
                
                
                
                
                
                
            
        
        