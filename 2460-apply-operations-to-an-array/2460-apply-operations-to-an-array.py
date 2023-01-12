class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for back in range(len(nums)):
            forw = back + 1
            
            if forw < len(nums) and nums[back] == nums[forw]:
                nums[back] *= 2
                nums[forw] = 0
                
                back += 2
        
        zeroPtr = 0
        numPtr = 0
        
        while numPtr < len(nums):
            if nums[numPtr] != 0:
                nums[numPtr], nums[zeroPtr] = nums[zeroPtr], nums[numPtr]
                
                zeroPtr += 1
            
            numPtr += 1
        
        return nums
        
        