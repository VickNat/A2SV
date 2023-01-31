class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p = len(players)-1
        t = len(trainers)-1
        counts = 0
        
        players.sort()
        trainers.sort()
        
        while t >= 0 and p >= 0:
            if players[p] > trainers[t]:
                p -= 1
            elif players[p] <= trainers[t]:
                p -= 1
                t -= 1
                counts += 1
            
            
        return counts