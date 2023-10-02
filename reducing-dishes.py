class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        N = len(satisfaction)
        satisfaction.sort()
        dp = [0]*N

        for i in range(N-1, -1, -1):
            time = 1
            for j in range(i, N):
                dp[i] += satisfaction[j]*(time)
                time += 1
        
        max_ = max(dp)

        return  max_ if max_ >= 0 else 0