class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
        self.memo[0] = 0
        self.memo[1] = self.memo[1] = 1
        self.max_ = 1
    
    def dp(self, n):
        if n in self.memo:
            return self.memo[n]
        
        if n%2 == 0:
            val = self.dp(n//2)
            self.memo[n] = val
            self.max_ = max(self.max_, self.memo[n])
            return self.memo[n]
        else:
            even = self.dp(n//2)
            odd = self.dp((n//2)+1)
            self.memo[n] = even+odd
            self.max_ = max(self.max_, self.memo[n])
            return self.memo[n]     

    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        while n > 1:
            self.dp(n)
            n -= 1
        
        return self.max_