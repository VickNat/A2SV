class Solution:
    def decodeString(self, s: str) -> str:

        def decoder(s, ptr, prevNum, current):
            while ptr < len(s):
                while s[ptr].isdigit():
                    prevNum *= 10
                    prevNum += int(s[ptr])
                    ptr += 1
                
                if s[ptr] == '[':
                    innerStr, nextPos = decoder(s, ptr+1, 0, '')
                    current += innerStr * prevNum
                    prevNum = 0
                    ptr = nextPos
                elif s[ptr] == ']':
                    return current, ptr
                else:
                    current += s[ptr]
                
                ptr += 1
            
            return current, ptr
        
        decodedStr, _ = decoder(s, 0, 0, '')
        return decodedStr