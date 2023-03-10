class Solution:
    def reverseFunction(self, s, left, right):
        if left >= right:
            return s
        
        s[left], s[right] = s[right], s[left]
        
        ans = self.reverseFunction(s, left+1, right-1)
        return ans
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseFunction(s, 0, len(s)-1)
            
        
            
        