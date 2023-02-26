class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        product = 1*nums[0]
        prefixSum = [1]*size
        
        for idx in range(1, size):
            prefixSum[idx] *= product
            product *= nums[idx]
                    
        product = 1*nums[-1]
        
        for idx in range(size-2, -1, -1):
            prefixSum[idx] *= product
            product *= nums[idx]
        
        return prefixSum            