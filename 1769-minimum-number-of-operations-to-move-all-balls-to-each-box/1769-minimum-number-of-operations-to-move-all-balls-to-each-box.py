class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxIdx = []
        operations = [0]*len(boxes)
        
        for idx in range(len(boxes)):
            if boxes[idx] == "1":
                boxIdx.append(idx)
        
        for box in range(len(boxes)):
            for index in boxIdx:
                if box == index:
                    continue
                else:
                    operations[box] += abs(index - box)
        
        return operations
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         operations = []
#         adjCounts = []
#         adjMoveSum = 0
        
#         for idx in range(len(boxes)):
#             ball = int(boxes[idx])
            
#             if ball == 1:
#                 adjMoveSum += idx
#                 adjCounts.append(idx)
        
#         for balls in range(len(boxes)):
#             totalMoves = abs(adjMoveSum - (len(adjCounts)*balls))
            
#             for elm in range(len(adjCounts)):
#                 if balls < len(boxes)-1 and balls >= adjCounts[elm]:
#                     totalMoves += adjCounts[elm]
            
#             operations.append(totalMoves)
            
#         return operations