class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        size = len(weights)

        def daysChecker(capacity):
            ptr = 0
            pack = 0
            day = 0

            while ptr < size:
                if pack + weights[ptr] > capacity:
                    day += 1
                    pack = 0
                
                pack += weights[ptr]

                if pack == capacity:
                    day += 1
                    pack = 0
                
                ptr += 1
            
            if pack != 0:
                day += 1
            
            return day

        left = max(weights)-1
        right = sum(weights)+1

        while left+1 < right:
            mid = left + (right-left)//2
            
            if daysChecker(mid) <= days:
                right = mid
            else:
                left = mid
        
        return right