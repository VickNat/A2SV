class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        idx = 0

        while idx < N:
            check = nums[idx]-1

            if check != idx and nums[check] != nums[idx]:
                nums[idx], nums[check] = nums[check], nums[idx]
            else:
                idx += 1
            
        for idx in range(0, N):
            check = nums[idx]-1

            if check != idx:
                ans.append(nums[idx])
        
        return ans