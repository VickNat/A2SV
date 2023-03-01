class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 0
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, -n)
            
        
        if n > 0:
            if n == 1:
                return x
            
            if n%2 == 0:
                ans = self.myPow(x, n/2)
                return ans*ans
            elif n%2 == 1:
                ans = self.myPow(x, (n-1)/2) 
                return ans*ans*x