class Solution: 
    # def select(self, arr, i):
    #     # code here 
    
    def selectionSort(self, arr,n):
        
        for elm in range(len(arr)):
            for idx in range(elm+1, len(arr)):
                if arr[elm] > arr[idx]:
                    arr[elm], arr[idx] = arr[idx], arr[elm]
        
        return arr
