class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = dict()
        
        for idx in range(len(nums)):
            if target - nums[idx] in dictionary:
                return [idx, dictionary[target - nums[idx]]]
            else:
                dictionary[nums[idx]] = idx
                
        
                