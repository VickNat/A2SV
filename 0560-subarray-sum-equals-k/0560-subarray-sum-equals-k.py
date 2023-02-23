class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        end = 0
        counts = defaultdict(int)
        total = 0
        subArr = 0
        
        for end in range(len(nums)):
            total += nums[end]
            
            if total == k:
                subArr += 1
            
            if total - k in counts:
                subArr += counts[total - k]
                
            counts[total] += 1
        
        return subArr
            
            
            
            
        
        
        