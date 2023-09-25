class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = defaultdict(int)

        def dfs(idx, curStones):
            if idx == len(stones):
                return abs(curStones)

            if (idx, curStones) in memo:
                return memo[(idx, curStones)]

            minWeight = min(dfs(idx+1, curStones+stones[idx]), dfs(idx+1, curStones-stones[idx]))

            memo[(idx, curStones)] = minWeight
            return minWeight
        
        return dfs(0, 0)