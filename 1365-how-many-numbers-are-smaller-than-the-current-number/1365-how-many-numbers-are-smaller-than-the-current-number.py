class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        
        for idx in nums:
            counts = 0
            
            for elm in range(len(nums)):
                if idx > nums[elm]:
                    counts += 1
            
            ans.append(counts)
        
        return ans