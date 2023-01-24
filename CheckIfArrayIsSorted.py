#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
    
        for elm in range(len(arr)-1):
            idx = elm + 1
            if arr[elm] > arr[idx]:
                return False
        
        return True
