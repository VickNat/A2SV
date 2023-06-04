class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        memo = [0]*(size+1)
        memo[0] = cost[0]
        memo[1] = cost[1]

        for i in range(2, size+1):
            memo[i] = min(memo[i-1], memo[i-2])

            if i != size:
                memo[i] += cost[i]
        
        return memo[-1]