class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friendsLeft = n
        friends = []
        
        for friend in range(1, n+1):
            friends.append(friend)
            
        idx = 0
        jumps = 1

        while friendsLeft > 1:
            
            if idx >= n:
                idx = 0
            
            if friends[idx] == -1:
                idx += 1
                continue
                
            if jumps == k:
                friends[idx] = -1
                friendsLeft -= 1
                jumps = 1
            elif jumps != k:
                jumps += 1
            
            idx += 1
                            
        for fr in friends:
            if fr != -1:
                return fr
        
                
                