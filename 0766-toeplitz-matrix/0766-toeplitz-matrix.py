class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r-1][c-1] != matrix[r][c]:
                    return False
            
        return True
        
        
        
        
        
        
        
        
#         for col in range(len(matrix)):
#             for row in range(len(matrix)-1):
#                 for r in range(row+1, len(matrix)):
#                     if matrix[row][col] != matrix[r][row]:
#                         return False
            
#         return True