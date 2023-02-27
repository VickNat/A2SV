class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        divDict = defaultdict(int)
        length = len(nums)
        subArr = 0
        sums = 0
        prefixSum = [0]
        
        divDict[0] += 1
        
        for idx in range(length):
            prefixSum.append(sums+nums[idx])
            sums += nums[idx]
            
            if prefixSum[idx+1]%k in divDict:
                subArr += divDict[prefixSum[idx+1]%k]
                
            divDict[prefixSum[idx+1]%k] += 1
                    
                
        return subArr