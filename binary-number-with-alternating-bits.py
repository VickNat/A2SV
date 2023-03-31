class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 0

        if n%2 == 0:
            prev = 1

        while n > 0:
            val =  1 & n

            if val and prev:
                return False
            elif not val and not prev:
                return False
                
            prev = val
            n >>= 1
        return True