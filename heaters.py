class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        N = len(houses)
        M = len(heaters)
        radius = 0
        cur = 0

        houses.sort()
        heaters.sort()

        for idx, val in enumerate(houses):
            curRadius = float('inf')
            
            for j in range(cur, M):
                pos = heaters[j]
                temp = abs(val-pos)
                
                if temp > curRadius:
                    break
                
                curRadius = temp
                cur = j
        
            radius = max(radius, curRadius)
        return radius