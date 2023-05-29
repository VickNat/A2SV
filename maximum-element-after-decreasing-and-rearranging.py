class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N = len(arr)
        arr.sort()

        for idx in range(N):
            if idx == 0:
                if arr[idx] != 1:
                    arr[idx] = 1
                continue
            
            if abs(arr[idx] - arr[idx-1]) > 1:
                arr[idx] = arr[idx-1]+1
        
        return arr[-1]