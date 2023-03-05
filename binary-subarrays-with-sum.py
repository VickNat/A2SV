class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total = 0
        prefixDict = defaultdict(int)
        prefixDict[total] = 1
        counts = 0
        size = len(nums)

        for elm in nums:
            total += elm
            if total-goal in prefixDict:
                counts += prefixDict[total-goal]
            
            prefixDict[total] += 1
        
        return counts