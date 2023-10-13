class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        lps = [0 for i in range(N)]
        pre = 0
        max_ = 0

        for i in range(1, N):
            while pre > 0 and s[i] != s[pre]:
                pre = lps[pre-1]
            
            if s[i] == s[pre]:
                pre += 1
                lps[i] = pre
                max_ = max(max_, lps[i])
        
        if lps[-1] > 0:
            return s[N-lps[-1]:]
        
        return ""