class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ptr = 0
        counts = 0
        size = len(nums)
        next_greater = [float('inf')]*size

        while counts < 2*size:
            if ptr == size:
                ptr = 0
            
            while stack and nums[stack[-1]] < nums[ptr]:
                next_greater[stack[-1]] = nums[ptr]
                stack.pop()
            
            if next_greater[ptr] == float('inf'):
                stack.append(ptr)
            
            ptr += 1
            counts += 1
        
        for idx in range(size):
            if next_greater[idx] == float('inf'):
                next_greater[idx] = -1
        
        return next_greater