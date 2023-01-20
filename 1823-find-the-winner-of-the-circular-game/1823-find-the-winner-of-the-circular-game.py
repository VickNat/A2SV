class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        counts = n
        friends = []
        
        for friend in range(1, n+1):
            friends.append(friend)
            
        idx = 0
        jumps = 1

        while counts > 1:
            
            if idx >= n:
                idx = 0
            
            if friends[idx] == -1:
                idx += 1
                continue
                
            if jumps == k:
                friends[idx] = -1
                counts -= 1
                jumps = 1
            elif jumps != k:
                jumps += 1
            
            idx += 1
                    
            
        winner = 0
        
        for fr in friends:
            if fr != -1:
                winner = fr
        
        return winner
                
                