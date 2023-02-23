class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0]*(len(nums)+1)
        
        for idx in range(1, len(nums)+1):
            self.prefixSum[idx] = self.prefixSum[idx-1] + nums[idx-1]
            
    def sumRange(self, left: int, right: int) -> int:
        total = self.prefixSum[right + 1] - self.prefixSum[left]
        
        return total
            
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)