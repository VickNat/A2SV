class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tmp = []
        idx = 0
        
        for idx in range(len(nums)+1):
            tmp.append(idx)
        
        temp = set(tmp)
        ans = set(nums)
        
        answer = temp.difference(ans)
        anss = list(answer)
        theAns = anss[0]
        
        return theAns
        