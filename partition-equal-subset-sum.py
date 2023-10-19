class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        total = sum(nums)
        nums.sort()
        
        if total%2 != 0:
            return False

        @cache
        def dp(idx, sum_):
            if idx == size:
                if sum_ == 0:
                    return True
                return False

            first = dp(idx+1, sum_+nums[idx])
            second = False
            if not first:
                second = dp(idx+1, sum_-nums[idx])

            return first or second
        
        return dp(0, 0)