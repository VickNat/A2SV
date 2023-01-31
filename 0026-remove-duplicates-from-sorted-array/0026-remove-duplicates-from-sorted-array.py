class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        counts = 0

        while right < len(nums) and nums[right] != -200:
            if right == left:
                right += 1
                continue
            
            if nums[left] == nums[right]:
                nums.pop(right)
                nums.append(-200)
            else:
                left = right
                right += 1
                        
        for num in nums:
            if num == -200:
                break
            else:
                counts += 1
    
        if counts == 0:
            counts += 1
            
        return counts