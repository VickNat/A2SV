class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        self.mat = [[0]*(cols + 1) for _ in range(rows + 1)]
        
        for r in range( rows):
            for c in range( cols):
                
                self.mat[r+1][c+1] = self.mat[r][c+1] + self.mat[r+1][c] - self.mat[r][c] + matrix[r][c]

                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        preSum = self.mat[row2+1][col2+1] - self.mat[row1][col2+1] - self.mat[row2+1][col1] + self.mat[row1][col1]
        
        return preSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)