class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        size = len(s)
        dp = [1]*(size+1)

        for i in range(size-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if i+1 < size and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        
        return dp[0]