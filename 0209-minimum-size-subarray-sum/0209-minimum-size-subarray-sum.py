class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = 0
        start = 0
        end = 0
        minLen = float('inf')
        
        for end in range(len(nums)):
            sums += nums[end]  
            
            if sums >= target:
                minLen = min(minLen, end - start + 1)
                
                while sums > target and start < end:
                    sums -= nums[start]
                    start += 1
                
                if sums < target:
                    start -= 1
                    sums += nums[start]
                
                minLen = min(minLen, end - start + 1)
                                
        if minLen == float('inf'):
            minLen = 0
            
        return minLen
            
            