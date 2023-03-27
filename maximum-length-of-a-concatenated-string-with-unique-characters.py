class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        ans = []

        def backtrack(valid, ptr):
            nonlocal ans

            if len(valid) > len(ans):
                ans = valid

            if ptr >= N:
                return
            
            cur = list(arr[ptr])

            if not valid or len(cur) == len(list(set(cur))):
                temp = valid + cur
                
                if len(list(set(temp))) == len(list(temp)):
                    backtrack(temp, ptr+1)

            backtrack(valid, ptr+1)
        
        backtrack([], 0)

        return len(ans)