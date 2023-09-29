class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxXor = 0
        mask = 0
        prefixes = set()
        N = len(nums)

        for i in range(30, -1, -1):
            mask |= (1 << i)
            newMax = maxXor | (1 << i)

            for i in range(N):
                prefixes.add(nums[i] & mask)
            
            for pre in prefixes:
                if pre^newMax in prefixes:
                    maxXor = newMax
            
            prefixes.clear()
        
        return maxXor