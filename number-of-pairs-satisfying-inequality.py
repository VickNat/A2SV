class Solution:
    def __init__(self):
        self.counts = 0

    def merge(self, leftArr, rightArr):
        ans = []
        L = len(leftArr)
        R = len(rightArr)
        l = 0
        r = 0

        while l < L and r < R:
            left = leftArr[l]
            right = rightArr[r]

            if left[0]-right[0] <= left[1]-right[1]+self.diff:
                self.counts += R-r
                l += 1
            else:
                r += 1

        
        l = 0
        r = 0

        while l < L and r < R:
            if leftArr[l][0]-leftArr[l][1] <= rightArr[r][0]-rightArr[r][1]:
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

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.diff = diff
        nums = list(zip(nums1, nums2))
        sort = self.mergeSort(0, len(nums)-1, nums)
        return self.counts