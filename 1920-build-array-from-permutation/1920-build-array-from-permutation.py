class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for idx in range(len(nums)):
            ans.append(nums[nums[idx]])
            
        return ans