#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        max_ = i
        l = 2*max_ + 1
        r = 2*max_ + 2
        
        if l < n and arr[l] > arr[max_]:
            max_ = l
        
        if r < n and arr[r] > arr[max_]:
            max_ = r
        
        if max_ != i:
            arr[i], arr[max_] = arr[max_], arr[i]
            self.heapify(arr, n, max_)
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)

    #Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        for idx in range(n-1, -1, -1):
            arr[0], arr[idx] = arr[idx], arr[0]
            self.heapify(arr, idx, 0)