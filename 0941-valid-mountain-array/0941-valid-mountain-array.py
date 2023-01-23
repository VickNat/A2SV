class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxVal = 0
        maxIdx = 0
        
        if len(arr) < 3:
            return False
        
        for i in range(len(arr)):
            if arr[i] > maxVal:
                maxVal = arr[i]
                maxIdx = i
        
        if maxIdx + 1 >= len(arr) or maxIdx == 0:
            return False
        
        right = maxIdx
        left = maxIdx
        
        while right < len(arr)-1:
            if arr[right] <= arr[right+1]:
                return False
            
            right += 1
        
        while left > 0:
            if arr[left] <= arr[left-1]:
                return False
            
            left -= 1
        
        return True