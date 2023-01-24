class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        bob = 0
        alice = len(piles)-1
        coins = 0
        
        piles.sort()
        
        while bob < alice-1:
            coins += piles[alice-1]
            
            bob += 1
            alice -= 2
            
        return coins