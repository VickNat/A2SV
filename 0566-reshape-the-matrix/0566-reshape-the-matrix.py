class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        arr = []
        
        if r*c != rows*cols:
            return mat
        
        for row in range(rows):
            for col in range(cols):
                arr.append(mat[row][col])
                
        ans = [[0]*c for _ in range(r)]
        ptr = 0
        
        for row in range(r):
            for col in range(c):
                ans[row][col] = arr[ptr]
                ptr += 1
        
        return ans
        
        