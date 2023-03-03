class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ptr = 0
        seconds = 0

        while tickets[k] != 0:
            if tickets[ptr] == 0:
                ptr += 1
            else:
                tickets[ptr] -= 1
                ptr += 1
                seconds += 1
            
            if ptr == len(tickets):
                ptr = 0
        
        return seconds