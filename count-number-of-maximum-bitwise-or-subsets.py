class Solution:
    def subsets(self, nums):
        powerSet = []
        N = len(nums)
        size = 2**(N)

        for val in range(size):
            subset = []
            idx = N-1
            cur = 1

            while cur <= val:
                if cur&val:
                    subset.append(nums[idx])
                
                idx -= 1
                cur <<= 1
            
            powerSet.append(subset)
        
        return powerSet

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subsets = self.subsets(nums)
        counts = 0
        maxOr = 0

        for elm in subsets:
            tempOr = 0

            for idx in range(len(elm)):
                tempOr |= elm[idx]
            
            if tempOr > maxOr:
                maxOr = tempOr
                counts = 1
            elif tempOr == maxOr:
                counts += 1
        
        return counts