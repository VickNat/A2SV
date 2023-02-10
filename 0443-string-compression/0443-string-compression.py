class Solution:
    def compress(self, chars: List[str]) -> int:
        answer = []
        right = 0
        left = 0
        size = len(chars)
        
        while left < size:
            answer.append(chars[left])
            
            right += 1
            counts = 1
            
            while right < size and chars[left] == chars[right]:
                counts += 1
                right += 1
            
            if counts > 1:
                temp = str(counts)

                i = 0
                while i < len(temp):
                    answer.append(temp[i])
                    i += 1
                
            left = right
        
        chars[:len(answer)+1] = answer[:]
        
        return len(answer)
            