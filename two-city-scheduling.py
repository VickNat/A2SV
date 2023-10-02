class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        memo = defaultdict(int)

        def dp(idx, a, b):
            if idx == N:
                if a == b:
                    return 0
                else:
                    return float('inf')
            
            if (idx, a, b) in memo:
                return memo[(idx, a, b)]
            
            ans = min(dp(idx+1, a+1, b)+costs[idx][0], dp(idx+1, a, b+1)+costs[idx][1])

            memo[(idx, a, b)] = ans
            return ans
        
        return dp(0, 0, 0)