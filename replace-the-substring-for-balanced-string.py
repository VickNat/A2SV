class Solution:
    def balancedString(self, s: str) -> int:
        import math
        freq = [0] * 26
        N = len(s)
        check = N // 4
        minStr = float('inf')
        balSubStr = defaultdict(int)
        temp = defaultdict(int)

        for idx in range(N):
            freq[ord(s[idx]) - ord('A')] += 1
        
        for i in range(26):
            if freq[i] > check:
                balance = freq[i] - check
                balSubStr[chr(i+ord('A'))] = balance

        l = 0
        for r in range(N):
            if s[r] in balSubStr:
                temp[s[r]] += 1

                while l <= r and all(temp[c] >= balSubStr[c] for c in balSubStr):
                    minStr = min(minStr, r-l+1)
                    temp[s[l]] -= 1
                    l += 1

        if minStr == float('inf'):
            return 0
        return minStr