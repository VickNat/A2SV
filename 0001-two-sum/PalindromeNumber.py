class Solution:
    #121
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        else:
            otherHalf = 0
            
            while x > otherHalf:
                otherHalf = (otherHalf*10) + x%10
                x//=10
                    
            if otherHalf == x or x == otherHalf//10:
                return True
            else:
                return False
                
