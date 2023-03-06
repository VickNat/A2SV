class Solution:
    def Winner(self, nums, left, right) -> int:
        if left == right:
            return nums[left]

        opt1 = self.Winner(nums, left+1, right)
        opt2 = self.Winner(nums, left, right-1)

        optLeft = nums[left] - opt1
        optRight = nums[right] - opt2

        if optLeft > optRight:
            return optLeft
        return optRight


    def PredictTheWinner(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums)-1

        ans = self.Winner(nums, left, right)

        return ans >= 0