class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        targetRow = 0
        
        for idx in range(rows):
            if matrix[idx][0] > target:
                targetRow = idx-1
                break
            elif matrix[idx][0] == target:
                return True
        
        for lastCheck in range(cols):
            if matrix[rows-1][lastCheck] == target:
                return True
        
        for col in range(cols):
            if matrix[targetRow][col] == target:
                return True
        
        return False