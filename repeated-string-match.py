class Solution:
    def checkSubstr(self, text, pattern):
        N = len(text)
        M = len(pattern)
        lps = [0 for i in range(len(pattern))]
        pre = 0

        for i in range(1, M):
            while pre > 0 and pattern[pre] != pattern[i]:
                pre = lps[pre-1]
            
            if pattern[pre] == pattern[i]:
                pre += 1
                lps[i] = pre
        
        j = 0
        for i in range(N):
            while j > 0 and pattern[j] != text[i]:
                j = lps[j-1]
            
            if pattern[j] == text[i]:
                j += 1
            
            if j == M:
                return True
        
        return False

    def repeatedStringMatch(self, a: str, b: str) -> int:
        newStr = a
        power = 10**4
        counts = 0
        maxLength = max(len(a), len(b))
        minLength = min(len(a), len(b))

        if self.checkSubstr(newStr, b):
            return len(newStr)//len(a)

        while len(newStr) <= power:
            newStr += a

            if len(newStr) > 3*maxLength:
                break
            if len(newStr) >= len(b):
                if self.checkSubstr(newStr, b):
                    return len(newStr)//len(a)

            counts += 1
        return -1