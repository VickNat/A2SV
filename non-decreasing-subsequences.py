class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        subSeq = set()

        def backtrack(ans, ptr):
            nonlocal subSeq
            if ptr >= N:
                return
            
            if nums[ptr] >= ans[-1]:
                subSeq.add(tuple(ans+[nums[ptr]]))
                backtrack(ans+[nums[ptr]], ptr+1)

            backtrack(ans, ptr+1)
        
        for idx in range(N-1):
            elm = nums[idx]
            backtrack([elm], idx+1)
        
        return subSeq