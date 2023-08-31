class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = defaultdict(int)
        size = len(nums)
        total = sum(nums)
        nums.sort()
        
        if total%2 != 0:
            return False

        def dp(idx, sum_):
            if idx == size:
                if sum_ == 0:
                    return True
                return False
            
            if (idx, sum_) in memo:
                return memo[(idx, sum_)]

            first = dp(idx+1, sum_+nums[idx])
            second = False
            if not first:
                second = dp(idx+1, sum_-nums[idx])

            memo[(idx, sum_)] = first or second
            return memo[(idx, sum_)]
        
        return dp(0, 0)