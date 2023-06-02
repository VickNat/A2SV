class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ans = [float('inf'), float('inf')]

        for num in nums:
            if num > ans[1]:
                return True
            if num > ans[0] and num < ans[1]:
                ans[1] = num
            elif num < ans[0]:
                ans[0] = num
        
        return False