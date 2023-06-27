class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        size = len(questions)
        dp = [0]*size
        
        for i in range(size-1, -1, -1):
            j = i + questions[i][1]+1
            cur = questions[i][0]
            
            if j < size:
                cur += dp[j]
            
            if i+1 < size:
                dp[i] = max(dp[i+1], cur)
            else:
                dp[i] = cur
        
        return dp[0]