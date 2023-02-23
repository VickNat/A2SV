class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        window = defaultdict(int)
        anagram = defaultdict(int)
        anIdx = []
        start = 0
        end = 0
        
        if len(p) > len(s):
            return anIdx
        
        for idx in range(len(p)):
            window[p[idx]] += 1        
        
        for end in range(len(s)):
            anagram[s[end]] += 1
            
            if end - start + 1 > k:
                if anagram[s[start]] > 1:
                    anagram[s[start]] -= 1
                else:
                    del anagram[s[start]]
                    
                start += 1
            
            
            if end - start + 1 == k and window == anagram:
                anIdx.append(start)
            
                
        return anIdx
            
            
            