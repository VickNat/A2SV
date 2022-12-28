class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest = []
        index = -1
        for idx in range(len(points)):
            if points[idx][0] == x or points[idx][1] == y:
                
                distance = abs(x-points[idx][0]) + abs(y-points[idx][1])
                
                if len(smallest) == 0:
                    smallest.append(distance)
                    index = idx
                
                if distance<smallest[-1] and len(smallest)!=0:
                    smallest.append(distance)
                    index = idx
        
        return index
                