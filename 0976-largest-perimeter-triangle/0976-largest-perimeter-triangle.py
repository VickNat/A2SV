class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        a_side = len(nums)-3
        c_side = len(nums)-1
        nums.sort()
        
        while a_side>=0:
            
            if nums[a_side]+nums[a_side+1]>nums[c_side]:
                return nums[a_side]+nums[a_side+1]+nums[c_side]
            else:
                a_side-=1
                c_side-=1
        
        return 0