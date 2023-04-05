class Solution:
    def minSteps(self, n: int) -> int:
        primeFactor = []
        d = 2
        
        while d*d <= n:
            while n%d == 0:
                primeFactor.append(d)
                n //= d
            
            d += 1
        
        if n > 1:
            primeFactor.append(n)
        
        return sum(primeFactor)