class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        idx = 0

        while idx < N:
            numIdx = nums[idx]-1

            if numIdx != idx and nums[numIdx] != nums[idx]:
                nums[numIdx], nums[idx] = nums[idx], nums[numIdx]
            else:
                idx += 1
        
        for idx in range(0, N):
            numIdx = nums[idx]-1
            
            if numIdx != idx:
                ans.append(idx+1)
        
        return ans