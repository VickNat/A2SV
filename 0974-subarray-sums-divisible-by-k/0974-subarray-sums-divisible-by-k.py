class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        divDict = defaultdict(int)
        length = len(nums)
        subArr = 0
        sums = 0
        prefixSum = [0]
        
        for idx in range(length):
            prefixSum.append(sums+nums[idx])
            sums += nums[idx]
        
        divDict[0] += 1
        
        for idx in range(1, length + 1):
            if prefixSum[idx]%k in divDict:
                subArr += divDict[prefixSum[idx]%k]
                
            divDict[prefixSum[idx]%k] += 1
                
        return subArr