class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        counts = -float('inf')
        less = False
        high = False
        left = 0
        right = 1
        size = len(arr)

        if size == 0:
            return 0

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
            elif less and not high:
                if arr[right] > arr[right-1]:
                    print(arr[right], arr[left])
                    less = False
                    high = True
                    right += 1
                elif arr[right] <= arr[right-1]:
                    counts = max(((right-1)-left)+1, counts)
                    left = right-1
                    less = False
                    high = False
            elif high and not less:
                if arr[right] < arr[right-1]:
                    
                    less = True
                    high = False
                    right += 1
                elif arr[right] >= arr[right-1]:
                    counts = max(((right-1)-left)+1, counts)
                    left = right-1
                    less = False
                    high = False
        
        counts = max(((right-1)-left)+1, counts)
        if counts == -float('inf'):
            return 1

        return counts