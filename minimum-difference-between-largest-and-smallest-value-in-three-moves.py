class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 4:
            return 0

        nums.sort()
        minDiff = float('inf')

        ptr = N-4
        for idx in range(N):
            if ptr >= N:
                break

            minDiff = min(minDiff, abs(nums[ptr]-nums[idx]))
            ptr += 1
        
        return minDiff