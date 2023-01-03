class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        counts = 0
        
        for idx in range(len(spaces)):
            answer += s[counts:spaces[idx]]+" "
            counts = spaces[idx]
            
        answer += s[counts:]
                                
        return answer