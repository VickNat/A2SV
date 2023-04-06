class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]
        ans = []

        def backtrack(val, path):
            if len(path) == n:
                ans.append(path)
                return
            
            for idx in range(n):
                temp = 1<<idx

                if val&temp == 0 and (nums[idx]%(len(path)+1) == 0 or (len(path)+1)%nums[idx] == 0):
                    val |= temp
                    backtrack(val, path+[nums[idx]])
                    val ^= temp
            
        backtrack(0, [])
        return len(ans)