class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        num_length = len(nums)
        prefixSum = [0]*(num_length+1)
        
        for req in requests:
            prefixSum[req[0]] += 1
            prefixSum[req[1]+1] -= 1
        
        sums = 0

        for idx in range(num_length+1):
            prefixSum[idx] += sums
            sums = prefixSum[idx]
        
        prefixSum.pop()
        prefixSum.sort()
        nums.sort()
        
        for idx in range(num_length):
            prefixSum[idx] *= nums[idx]
        
        total = sum(prefixSum)
        
        return total%(10**9 + 7)
    