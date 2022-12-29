class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        checkList = []
        
        for idx in range(n):
            checkList.append(idx)
            
        for elm in range(len(checkList)):
            if checkList[elm] not in nums:
                return checkList[elm]
        