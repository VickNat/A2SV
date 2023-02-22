class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = defaultdict(int)
        ans = []
        maxIdx = -1
        preSum = 0
        
        for idx in range(len(s)):
            occur[s[idx]] = idx
        
        for idx in range(len(s)):
            maxIdx = max(occur[s[idx]], maxIdx)
            
            if idx == maxIdx:
                size = idx - preSum + 1
                preSum += size
                ans.append(size)
            
            
        
        return ans
            