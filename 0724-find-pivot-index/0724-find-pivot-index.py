class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = [0]
        acc = 0
        
        for num in nums:
            acc += num
            preSum.append(acc)
        
        for i in range(1, len(preSum)):
            if preSum[i-1] == preSum[-1] - preSum[i]:
                return i-1
            
        return -1
        