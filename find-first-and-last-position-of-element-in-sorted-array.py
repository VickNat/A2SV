class Solution:
    def rightSearch(self, target, left, right, arr):
        while left <= right:
            mid = (left + right)//2

            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                while mid < len(arr) and arr[mid] == target:
                    mid += 1
                
                return mid - 1
            
        return -1

    def leftSearch(self, target, left, right, arr):
        while left <= right:
            mid = (left + right)//2

            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                while mid >= 0 and arr[mid] == target:
                    mid -= 1
                
                return mid + 1
            
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = [-1, -1]

        ans[0] = self.leftSearch(target, left, right, nums)
        ans[1] = self.rightSearch(target, left, right, nums)

        return ans