class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        distance = float('-inf')
        
        for elm in trips:
            distance = max(distance, elm[-1])
        
        prefixSum = [0]*(distance+2)
        sums = 0
        
        for elm in trips:
            prefixSum[elm[1]+1] += elm[0]
            prefixSum[elm[2]+1] -= elm[0]
        
        for idx in range(1, len(prefixSum)):
            sums += prefixSum[idx]
            prefixSum[idx] = sums
            
            if prefixSum[idx] > capacity:
                return False
        
        return True