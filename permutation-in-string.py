class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = defaultdict(int)
        perm = defaultdict(int)
        start = 0
        end = 0
        size = len(s1)
        
        for idx in range(len(s1)):
            window[s1[idx]] += 1
                        
        for end in range(len(s2)):
            perm[s2[end]] += 1
                
            if end - start + 1 > size:
                perm[s2[start]] -= 1
                
                if perm[s2[start]] == 0:
                    del perm[s2[start]]
                    
                start += 1
                
            if window == perm:
                return True
            
        return False