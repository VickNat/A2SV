class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        N = len(nums)

        def dp(curSum, path, idx):
            if len(path) == N:
                if curSum == 0:
                    return 1
                return 0
            
            if (curSum, tuple(path)) in memo:
                return memo[(curSum, tuple(path))]
            
            val = 0
            val += dp(curSum-nums[idx], path[:]+[nums[idx]], idx+1)
            val += dp(curSum+nums[idx], path[:]+[nums[idx]], idx+1)
            
            memo[(curSum, tuple(path))] = val
            return memo[(curSum, tuple(path))]
        
        ans = dp(target, [], 0)
        return ans