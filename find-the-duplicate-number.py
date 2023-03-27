class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        idx = 0

        while idx < N:
            check = nums[idx]-1

            if check != idx and nums[check] != nums[idx]:
                nums[idx], nums[check] = nums[check], nums[idx]
            else:
                idx += 1
        
        return nums[-1]