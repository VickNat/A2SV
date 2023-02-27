class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        divDict = defaultdict(int)
        length = len(nums)
        subArr = 0
        sums = 0
        
        divDict[0] += 1
        
        for idx in range(length):
            sums += nums[idx]
            
            if sums%k in divDict:
                subArr += divDict[sums%k]
                
            divDict[sums%k] += 1
                    
                
        return subArr