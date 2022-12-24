class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_index = 0
        
        for i in nums:
            if i%2 == 0:
                temp = nums[odd_index]
                nums[odd_index] = i
                i = temp
                
                odd_index += 1
                
        return nums
        
