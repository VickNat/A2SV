class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = 0
        maxAvg = float('-inf')
        total = 0
        
        for end in range(len(nums)):
            total += nums[end]
            
            if end - start + 1 > k:
                total -= nums[start]
                start += 1
                
            if end - start + 1 == k:
                avg = total/k
                maxAvg = max(avg, maxAvg)
        
        return maxAvg