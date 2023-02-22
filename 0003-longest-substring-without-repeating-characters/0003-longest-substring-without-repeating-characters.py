class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        left = 0
        right = 0
        size = 0
        
        while right < len(s):
            if s[right] not in ans:
                ans.add(s[right])
                right += 1
            else:
                while s[right] in ans:
                    ans.remove(s[left])
                    left += 1
                    
            size = max(size, len(ans))
            
            
        
        return size