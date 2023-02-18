class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        
        k %= size
        
        counts = 0
        rotate = size - 1
        
        while counts < k:
            temp = nums[rotate]
            
            nums.insert(0, temp)
            nums.pop()
            
            nums[0] = temp
            counts += 1
        