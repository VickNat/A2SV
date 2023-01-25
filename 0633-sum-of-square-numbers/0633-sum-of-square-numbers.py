class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        
        while left <= c:
            cSum = c - left*left
            if cSum < 0:
                return False
            
            right = sqrt(cSum)
            
            if int(right + 0.5)**2 == (cSum):
                return True
            
            left += 1
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         left = 0
#         right = c
        
#         while left <= right:
#             leftSquare = left*left
#             rightSquare = right*right
#             cSum = leftSquare + rightSquare
            
#             if cSum > c:
#                 right -= 1
#             elif cSum < c:
#                 left += 1
#             else:
#                 return True
        
#         return False
        