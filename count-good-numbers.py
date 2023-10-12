class Solution:
    def binaryExponent(self, x, y, mod):
        res = 1

        while y > 0:
            if y&1:
                res *= x%mod
            
            x *= x%mod
            y >>= 1
        
        return res % mod

    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        res = 0
        
        if n%2 == 0:
            res = self.binaryExponent(20, n//2, mod)
        else:
            oddNums = n//2
            evenNums = n-oddNums

            odd = self.binaryExponent(4, oddNums, mod)
            even = self.binaryExponent(5, evenNums, mod)

            res = (even*odd)%mod
    
        return res