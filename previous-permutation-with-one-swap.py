class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        N = len(arr)
        index = N-2

        while index >= 0:
            if arr[index] <= arr[index+1]:
                index -= 1
            else:
                break
        
        if index >= 0:
            maxIdx = index+1
            for idx in range(index+1, N):
                if arr[idx] > arr[maxIdx] and arr[idx] < arr[index]:
                    maxIdx = idx
            
            arr[index], arr[maxIdx] = arr[maxIdx], arr[index]
        
        return arr