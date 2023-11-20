class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        
        def dp(idx, flag):
            if idx >= len(prices):
                return 0
            
            if (idx, flag) in memo:
                return memo[(idx, flag)]
            
            maxProfit = 0
            if not flag:
                maxProfit = max(dp(idx+1, True) - prices[idx], dp(idx+1, False))
            else:
                maxProfit = max(prices[idx], dp(idx+1, True))
            
            memo[(idx, flag)] = maxProfit
            return maxProfit
        
        return dp(0, False)