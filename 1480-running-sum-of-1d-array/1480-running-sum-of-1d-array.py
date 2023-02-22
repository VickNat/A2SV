class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = 0
        preSum = []
        
        for num in nums:
            running += num
            preSum.append(running)
        
        return preSum