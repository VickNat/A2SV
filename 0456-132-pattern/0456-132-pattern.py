class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        ptr = len(nums)-1
        hold = -float('inf')
        
        while ptr >= 0:
            if stack and stack[-1] > nums[ptr] and hold > nums[ptr]:
                print(stack)
                return True
            while stack and stack[-1] < nums[ptr]:
                hold = stack[-1]
                stack.pop()
                
            
            
            stack.append(nums[ptr])
            
            ptr -= 1
            
        return False
                
                