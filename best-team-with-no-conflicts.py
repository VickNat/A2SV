class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sortedArr = []
        N = len(scores)
        memo = defaultdict(int)

        if N == 1:
            return scores[0]

        for i in range(N):
            sortedArr.append((ages[i], scores[i]))

        sortedArr.sort()

        for i in range(N):
            scores[i] = sortedArr[i][1]
            ages[i] = sortedArr[i][0]
        
        memo[0] = scores[0]

        def dp(i):
            if i in memo:
                return memo[i]
            
            score = scores[i]
            max_ = 0
            for idx in range(i-1, -1, -1):
                if scores[i] >= scores[idx]:
                    max_ = max(max_, dp(idx))
            
            score += max_
            memo[i] = score
            return score
        
        ans = 0
        for i in range(N-1, -1, -1):
            ans = max(ans, dp(i))
        
        return ans