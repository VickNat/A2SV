class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroPtr = 0
        numPtr = 0
        
        while numPtr < len(nums):
            if nums[numPtr] != 0:
                nums[zeroPtr], nums[numPtr] = nums[numPtr], nums[zeroPtr]
                zeroPtr += 1
            
            numPtr += 1
                
                
        
        
        
        
        
        
        
        
        
        
        
        

        
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 # temp = nums[i]
#                 # nums[j] = nums[i]
#                 # nums[j] = temp
# #                 Swap them
#                 nums[i], nums[j] = nums[j], nums[i]
                
#                 j += 1
        