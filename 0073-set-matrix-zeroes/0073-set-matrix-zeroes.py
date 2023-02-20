class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        record = []
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                temp = []
                
                if matrix[r][c] == 0:
                    temp.append(r)
                    temp.append(c)
                    record.append(temp)
        
        for idx in range(len(record)):
            row = 0
            col = 0
            rRow = record[idx][0]
            rCol = record[idx][1]
            
            while col < cols:
                matrix[rRow][col] = 0
                col += 1
            
            while row < rows:
                matrix[row][rCol] = 0
                row += 1
        