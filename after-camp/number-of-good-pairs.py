class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = defaultdict(int)
        ans = 0

        for num in nums:
            if num in pairs:
                ans += pairs[num]
            
            pairs[num] += 1
        
        return ans