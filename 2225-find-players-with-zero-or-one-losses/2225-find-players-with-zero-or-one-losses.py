class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        playerPoints = dict()
        wins = []
        losses = []
        answer = []
        
        for players in range(len(matches)):
            winIdx = matches[players][0]
            lossIdx = matches[players][1]
            
            if winIdx not in playerPoints.keys():
                playerPoints[winIdx] = 0
            # elif playerPoints[winIdx] == 0:
            #     continue
            
            if lossIdx not in playerPoints.keys():
                playerPoints[lossIdx] = 1
            elif playerPoints[lossIdx] >= 0:
                playerPoints[lossIdx] += 1
        
        for result in playerPoints.keys():
            if playerPoints[result] == 0:
                wins.append(result)
            elif playerPoints[result] == 1:
                losses.append(result)
            else:
                continue
        
        wins.sort()
        losses.sort()
        answer.append(wins)
        answer.append(losses)
        
        return answer