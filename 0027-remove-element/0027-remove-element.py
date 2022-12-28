class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_list = []
        
        for idx in range(len(nums)):
            if nums[idx] == val:
                index_list.append(idx)
                
        index_list.reverse()
        
        for index in index_list:
            nums.pop(index)
        
        return len(nums)