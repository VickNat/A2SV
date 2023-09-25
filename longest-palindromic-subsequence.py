class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        reverse = s[::-1]
        dp = [[0]*(N+1) for _ in range(N+1)]

        for i in range(N):
            for j in range(N):
                if s[i] == reverse[j]:
                    dp[i+1][j+1] = 1+dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[-1][-1]