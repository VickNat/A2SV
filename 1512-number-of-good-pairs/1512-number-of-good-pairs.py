class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair1 = 0
        counts = 0
        
        for pair1 in range(len(nums)):
            
            pair2 = pair1+1
            
            while pair2<len(nums):
                
                if nums[pair1]==nums[pair2]:
                    counts+=1
                
                pair2+=1
        
        return counts