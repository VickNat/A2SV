class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_length = len(arr)
        index = 0
        
        while index<arr_length:
            if arr[index] == 0:
                arr.insert(index+1, 0)
                index += 1
                arr.pop()
            index += 1
                
