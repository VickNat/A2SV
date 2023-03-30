class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        shifts = 0

        while num > 0:
            val = 0

            if num & 1 == 0:
                val = 1
                val <<= shifts

            complement |= val
            num >>= 1
            shifts += 1
        
        return complement