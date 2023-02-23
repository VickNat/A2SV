class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = set()
        start = 0
        end = 0
        maxSubStr = 0
        
        for end in range(len(s)):
            
            if s[end] in subStr:
                maxSubStr = max(maxSubStr, len(subStr))
                
                while s[end] in subStr:
                    subStr.remove(s[start])
                    start += 1
                
            subStr.add(s[end])
        
        maxSubStr = max(maxSubStr, len(subStr))
        
        return maxSubStr