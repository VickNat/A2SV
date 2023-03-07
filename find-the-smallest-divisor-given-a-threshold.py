class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1]+1

        while left+1 < right:
            mid = left+(right-left)//2
            sums = 0

            for elm in nums:
                sums += ceil(elm/mid)

            if sums <= threshold:
                right = mid
            else:
                left = mid
        
        return right