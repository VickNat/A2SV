class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        pre = 1
        preSumRight = [1]*(size)
        preSumLeft = [1]*(size)
        
        for idx in range(size):
            if idx == 0:
                preSumRight[idx] = 1
                continue
            
            preSumRight[idx] *= nums[idx - 1] * pre
            pre *= nums[idx - 1]
        
        pre = 1
        
        for idx in range(size-1, -1, -1):                
            if idx == size - 1:
                preSumLeft[idx] = 1
                continue
            
            preSumLeft[idx] *= nums[idx + 1] * pre
            pre *= nums[idx + 1]
        
        for idx in range(size):
            nums[idx] = preSumRight[idx] * preSumLeft[idx]
        
        return nums
            