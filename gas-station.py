class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        neg = 0
        pos = 0
        idx = -1
        diff = [gas[i]-cost[i] for i in range(N)]

        for i in range(N):
            cur = diff[i]

            if idx == -1:
                if cur < 0:
                    neg += cur
                elif cur >= 0:
                    pos += cur
                    idx = i
            else:
                if cur < 0:
                    pos += cur

                    if pos < 0:
                        idx = -1
                        neg += pos
                        pos = 0
                else:
                    pos += cur
        
        if pos + neg < 0:
            return -1

        return idx