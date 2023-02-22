class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        window = defaultdict(int)
        comp = defaultdict(int)
        ans = []
        start = 0
        end = 0
        
        if len(p) > len(s):
            return ans
        
        for idx in range(len(p)):
            window[p[idx]] += 1        
        
        while end < k:
            comp[s[end]] += 1
            end += 1
            
        end -= 1
        while start <= len(s) - k and end <= len(s):
            if start != 0:
                comp[s[end]] += 1
                
            if comp == window:
                ans.append(start)
            
            if comp[s[start]] == 1:
                del comp[s[start]]
            else:
                comp[s[start]] -= 1
            
            end += 1
            start += 1
        return ans
            
            
            