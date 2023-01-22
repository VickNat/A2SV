class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        m, ans = defaultdict(int), 0
        
        for i in range(len(nums)):
            
            ans += i - m[nums[i] - i]
            m[nums[i] - i] += 1
            
        return ans
            