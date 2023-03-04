class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        counts = 1
        less = False
        high = False
        left = 0
        right = 0
        size = len(arr)

        while right < size:
            if not less and not high:
                if arr[right] < arr[right-1]:
                    less = True
                    high = False
                elif arr[right] > arr[right-1]:
                    less = False
                    high = True
                else:
                    left += 1
                
                counts = max((right-left)+1, counts)
                right += 1
            elif less and not high and arr[right] > arr[right-1]:
                less = False
                high = True
                right += 1                    
            elif high and not less and arr[right] < arr[right-1]:
                less = True
                high = False
                right += 1
            elif arr[right] >= arr[right-1] or arr[right] <= arr[right-1]:
                counts = max(((right-1)-left)+1, counts)
                left = right-1
                less = False
                high = False
        
        counts = max(((right-1)-left)+1, counts)

        return counts