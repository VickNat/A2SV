class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(i, path):
            if sum(path) == target:
                combinations.append(path[:])
                return
            
            if i >= len(candidates) or sum(path) > target:
                return

            backtrack(i, path+[candidates[i]])
            backtrack(i+1, path)

        backtrack(0, [])
        return combinations