class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = 0
        idx = len(arr)-1
        
        while idx >= 0:
            if idx == len(arr)-1:
                rightMax = arr[idx]
                arr[idx] = -1
            else:
                temp = arr[idx]
                arr[idx] = rightMax
                rightMax = max(rightMax, temp)
                
            idx -= 1
        
        return arr
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # maxRight = 0
        
#         for elm in range(len(arr)):
#             if elm == len(arr) - 1:
#                 arr[elm] = -1
#                 break
            
#             maxRight = max(arr[elm+1:])
            
#             arr[elm] = maxRight
                
#         return arr