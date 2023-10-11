class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        occur = list(set(nums))
        occur.sort()
        minOperations = float('inf')

        for i in range(len(occur)):
            start = occur[i]
            end = start+(N-1)

            left = 0
            right = len(occur)-1

            while left <= right:
                mid = (left+right)//2

                if occur[mid] <= end:
                    left = mid+1
                else:
                    right = mid-1
            
            minOperations = min(minOperations, N-(left-i))

        return minOperations