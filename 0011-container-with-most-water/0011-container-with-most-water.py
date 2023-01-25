class Solution:
    def maxArea(self, height: List[int]) -> int:
        waterAmount = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            container = (min(height[right], height[left])) * (right-left)
            
            waterAmount = max(waterAmount, container)
            
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
            
        return waterAmount