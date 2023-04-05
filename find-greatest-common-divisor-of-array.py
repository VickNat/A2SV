class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)

        def gcd(a, b):
            if a%b == 0:
                return b
            return gcd(b, a%b)
        
        return gcd(max_, min_)