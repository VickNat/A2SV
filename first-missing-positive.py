class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        idx = 0

        while idx < N:
            check = nums[idx]-1

            if check < N and check >= 0 and check != idx and nums[check] != nums[idx]:
                nums[check], nums[idx] = nums[idx], nums[check]
            else:
                idx += 1
        
        for idx in range(0, N):
            check = nums[idx]-1

            if check != idx:
                return idx+1
        
        return N+1