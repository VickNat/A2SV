class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        left = 0
        right = 0
        size = 0
        
        while right < len(s):
            if s[right] in ans:
                while s[right] in ans:
                    ans.remove(s[left])
                    left += 1
                
            ans.add(s[right])                
                    
            size = max(size, len(ans))
            
            right += 1
        
        return size