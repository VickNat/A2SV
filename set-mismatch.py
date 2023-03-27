class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        idx = 0

        while idx < N:
            check = nums[idx]-1

            if check != idx and nums[check] != nums[idx]:
                nums[check], nums[idx] = nums[idx], nums[check]
            else:
                idx += 1
        
        for idx in range(N):
            check = nums[idx]-1

            if check != idx:
                return [check+1, idx+1]