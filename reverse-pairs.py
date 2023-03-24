class Solution:
    def __init__(self):
        self.counts = 0
    
    def merge(self, leftArr, rightArr):
        ans = []
        L = len(leftArr)
        R = len(rightArr)
        right = R-1
        left = L-1

        while right >= 0 and left >= 0:

            while right >= 0 and leftArr[left] <= 2*(rightArr[right]):
                right -= 1
            
            if right >= 0 and 2*(rightArr[right]) < leftArr[left]:
                self.counts += right+1
                
            left -= 1
        
        l = 0
        r = 0

        while l < L and r < R:
            if leftArr[l] <= rightArr[r]:
                ans.append(leftArr[l])
                l += 1
            else:
                ans.append(rightArr[r])
                r += 1
        
        while l < L:
            ans.append(leftArr[l])
            l += 1
        
        while r < R:
            ans.append(rightArr[r])
            r += 1
        
        return ans

    def mergeSort(self, left, right, nums):
        if left == right:
            return [nums[left]]
        
        mid = left + (right-left)//2

        leftArr = self.mergeSort(left, mid, nums)
        rightArr = self.mergeSort(mid+1, right, nums)

        return self.merge(leftArr, rightArr)

    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(0, len(nums)-1, nums)
        return self.counts