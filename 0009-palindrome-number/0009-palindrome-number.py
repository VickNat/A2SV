class Solution:
    #121
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x<=9:
            return True
        
        pal = str(x)
        left = 0
        right = len(pal)-1
        
        while left<=right:
            if left == right:
                return True
            elif pal[left]==pal[right]:
                    left+=1
                    right-=1
            elif pal[left]!=pal[right]:
                return False
            
        return True
                    