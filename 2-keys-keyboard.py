class Solution:
    def minSteps(self, n: int) -> int:
        memo = defaultdict(int)

        def dp(curStr, copied):
            if len(curStr) == n:
                return 1

            if len(curStr) > n:
                return float('inf')

            if (curStr, copied) in memo:
                return memo[(curStr, copied)]
            
            minOperation = float('inf')

            if len(curStr) == len(copied):
                minOperation = dp(curStr+copied, copied)
            else:
                minOperation = min(dp(curStr+copied, copied), dp(curStr, curStr))

            memo[(curStr, copied)] = minOperation+1
            return minOperation+1
        
        ans = dp("A", "A")
        return ans if ans > 1 else 0