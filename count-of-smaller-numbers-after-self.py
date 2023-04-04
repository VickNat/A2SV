class Solution:

    def merge(self, lArr, rArr):
        lSize = len(lArr)
        rSize = len(rArr)
        smallCounts = [0]*lSize
        l = 0
        r = 0

        while l < lSize and r < rSize:
            left = lArr[l][0]
            right = rArr[r][0]

            if left > right:
                smallCounts[l] += 1
                r += 1
            else:
                l += 1
        
        result = list(accumulate(smallCounts))

        for idx in range(0, lSize):
            left = lArr[idx][1]
            self.smaller[left] += result[idx]
        
        l = 0
        r = 0
        merged = []

        while l < lSize and r < rSize:
            if lArr[l][0] <= rArr[r][0]:
                merged.append(lArr[l])
                l += 1
            else:
                merged.append(rArr[r])
                r += 1

        while l < lSize:
            merged.append(lArr[l])
            l += 1

        while r < rSize:
            merged.append(rArr[r])
            r += 1
        
        return merged


    def mergeSort(self, left, right, nums):
        if left == right:
            return [nums[left]]
        
        mid = left + (right-left)//2

        left_half = self.mergeSort(left, mid, nums)
        right_half = self.mergeSort(mid+1, right, nums)

        return self.merge(left_half, right_half)

    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        self.smaller = [0]*N
        numbers = []

        for idx in range(N):
            numbers.append([nums[idx], idx])
        
        self.mergeSort(0, N-1, numbers)

        return self.smaller