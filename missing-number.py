class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        idx = 0

        while idx < N:
            check = nums[idx]-1

            if check >= 0 and check != idx:
                nums[check], nums[idx] = nums[idx], nums[check]
            else:
                idx += 1

        for i in range(N):
            if nums[i] != i+1:
                return i+1
        return 0