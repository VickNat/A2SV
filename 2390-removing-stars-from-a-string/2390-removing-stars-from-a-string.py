class Solution:
    def removeStars(self, s: str) -> str:
        ptr = 0
        length = len(s)
        stack = []
        
        while ptr < length:
            if s[ptr] != "*":
                stack.append(s[ptr])
            else:
                stack.pop()
            
            ptr += 1
        
        return "".join(stack)