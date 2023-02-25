class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        ptr = 0
        num = 0
        symbols = defaultdict(int)
        symbols['I'] = 1
        symbols['V'] = 5
        symbols['X'] = 10
        symbols['L'] = 50
        symbols['C'] = 100
        symbols['D'] = 500
        symbols['M'] = 1000
        
        while ptr < length:
            if ptr + 1 < length and symbols[s[ptr]] < symbols[s[ptr + 1]]:
                num += symbols[s[ptr + 1]] - symbols[s[ptr]]
                ptr += 2
                continue
            
            num += symbols[s[ptr]]
            ptr += 1
        
        return num