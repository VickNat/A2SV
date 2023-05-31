class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)

        def dp(target):
            if target == 0:
                return 0
            if target < 0:
                return float('inf')
            
            if target in memo:
                return memo[target]

            min_ = float('inf')
            for elm in coins:
                cur = target-elm
                val = dp(cur)
                min_ = min(min_, val)

            memo[target] = min_+1
            return min_+1
                
        dp(amount)
        return memo[amount] if memo[amount] != float('inf') else -1