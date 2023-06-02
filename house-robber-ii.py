class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        max_ = max(nums)

        if N <= 3:
            return max(nums)

        memo = [0]*N
        memo[0] = nums[0]
        memo[1] = nums[1]
        memo[2] = nums[0]+nums[2]
        max_ = max(max_, memo[2])

        for i in range(3, N-1):
            memo[i] = max(memo[i-2]+nums[i], memo[i-3]+nums[i])
            max_ = max(max_, memo[i])
        
        memo = [0]*N
        memo[1] = nums[1]
        memo[2] = nums[2]
        memo[3] = nums[1] + nums[3]
        max_ = max(max_, memo[3])

        for i in range(4, N):
            memo[i] = max(memo[i-2]+nums[i], memo[i-3]+nums[i])
            max_ = max(max_, memo[i])
        
        return max_