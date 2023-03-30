class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ham_distance = 0

        while x > 0 or y > 0:
            x_bit = x & 1
            y_bit = y & 1

            if x_bit != y_bit:
                ham_distance += 1
            
            x >>= 1
            y >>= 1
        
        return ham_distance