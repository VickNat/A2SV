class Solution:
    def rightSearch(self, target, left, right, arr):
        while left <= right:
            mid = (left + right)//2

            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

    def leftSearch(self, target, left, right, arr):
        while left <= right:
            mid = (left + right)//2

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = [-1, -1]

        ans[0] = self.leftSearch(target, left, right, nums)
        ans[1] = self.rightSearch(target, left, right, nums)

        if ans[0] >= len(nums) or nums[ans[0]] != target:
            ans[0] = -1
        if ans[1] < 0 or nums[ans[1]] != target:
            ans[1] = -1

        return ans