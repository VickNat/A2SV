class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        mutate = []
        N = len(nums)

        def backtrack(val, path):
            if len(path) == N:
                mutate.append(path)
                return
            
            for idx in range(N):
                temp = 1 << idx

                if temp & val == 0:
                    val = temp | val
                    backtrack(val, path+[nums[idx]])
                    val = temp ^ val
        
        backtrack(0, [])
        return mutate