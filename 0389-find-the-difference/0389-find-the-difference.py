class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor_str = 0
        
        for s_xor in s:
            xor_str ^= ord(s_xor)
        
        for t_xor in t:
            xor_str ^= ord(t_xor)
        
        return chr(xor_str)
                    
                
                