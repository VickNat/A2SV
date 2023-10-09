class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)-1

        for left in range(len(haystack)-right):
            if haystack[left:right+1] == needle:
                return left
            
            right += 1
        
        return -1