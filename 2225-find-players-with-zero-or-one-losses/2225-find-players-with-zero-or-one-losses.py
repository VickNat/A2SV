class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        playerPoints = dict()
        wins = []
        losses = []
        answer = []
        
#         using range function in for loops uses less memory
        
        for players in matches:
            winIdx = players[0]
            lossIdx = players[1]
            
            if winIdx not in playerPoints:
                playerPoints[winIdx] = 0
                
#             If i insert the elif below, it'll skip the loss test as well
            # elif playerPoints[winIdx] == 0:
            #     continue
            
            if lossIdx not in playerPoints:
                playerPoints[lossIdx] = 1
            elif playerPoints[lossIdx] >= 0:
                playerPoints[lossIdx] += 1
        
        for result in playerPoints:
            if playerPoints[result] == 0:
                wins.append(result)
            elif playerPoints[result] == 1:
                losses.append(result)
        
        wins.sort()
        losses.sort()
        answer.append(wins)
        answer.append(losses)
        
        return answer