class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        size = len(triangle)

        for i in range(1, size):
            cur = triangle[i]
            for j in range(len(cur)):
                val = float('inf')
                if j < len(triangle[i-1]):
                    val = min(val, triangle[i-1][j])
                
                if j-1 >= 0:
                    val = min(val, triangle[i-1][j-1])
                
                triangle[i][j] += val
        
        return min(triangle[-1])