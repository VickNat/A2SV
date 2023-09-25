class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = defaultdict(int)

        def dp(i, curStones):
            if i == len(stones):
                return abs(curStones)
            
            if (i, curStones) in memo:
                return memo[(i, curStones)]
            
            minWeight = min(dp(i+1, curStones+stones[i]), dp(i+1, curStones-stones[i]))

            memo[(i, curStones)] = minWeight
            return minWeight
        
        return dp(0, 0)