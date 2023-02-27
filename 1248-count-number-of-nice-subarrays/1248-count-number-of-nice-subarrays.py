class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddDict = defaultdict(int)
        odds = [0]
        length = len(nums)
        score = 0
        
        for idx in range(length):
            if nums[idx]%2 != 0:
                odds.append(1)
            else:
                odds.append(0)
            
            odds[-1] += odds[idx]
            oddDict[odds[idx]] += 1
        
        oddDict[odds[-1]] += 1
        
        for idx in range(length + 1):
            if odds[idx] - k in oddDict:
                score += oddDict[odds[idx] - k]
        
        return score
        
            