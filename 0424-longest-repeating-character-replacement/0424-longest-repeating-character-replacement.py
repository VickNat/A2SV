class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        repeat = defaultdict(int)
        size = len(s)
        maxLength = 0
        
        for end in range(size):
            repeat[s[end]] += 1
            frequent = max(repeat.values())
            
            while (end - start + 1) - frequent > k:
                repeat[s[start]] -= 1
                start += 1
                
                if repeat[s[start]] == 0:
                    repeat.pop(s[start])
                
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength