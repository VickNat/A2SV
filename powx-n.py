class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        y = abs(n)

        while y > 0:
            if y&1:
                if n < 0:
                    res /= x
                else:
                    res *= x
            
            x *= x
            y >>= 1
        
        return res