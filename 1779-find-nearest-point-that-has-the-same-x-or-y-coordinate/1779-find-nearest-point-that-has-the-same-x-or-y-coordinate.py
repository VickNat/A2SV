class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDist = []
        minIdx = -1
        
        for point in range(len(points)):
            xIdx = points[point][0]
            yIdx = points[point][1]
            
            if x == xIdx or y == yIdx:
                distance = abs(x-xIdx) + abs(y-yIdx)
                
                if len(minDist) == 0:
                    minDist.append(distance)
                    minIdx = point
                
                elif minDist[-1]>distance:
                    minDist.append(distance)
                    minIdx = point
                
        return minIdx
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         smallest = []
#         index = -1
#         for idx in range(len(points)):
#             if points[idx][0] == x or points[idx][1] == y:
                
#                 distance = abs(x-points[idx][0]) + abs(y-points[idx][1])
                
#                 if len(smallest) == 0:
#                     smallest.append(distance)
#                     index = idx
                
#                 if distance<smallest[-1] and len(smallest)!=0:
#                     smallest.append(distance)
#                     index = idx
        
#         return index
                