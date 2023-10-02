class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            while stack and stack[-1][1] == k:
                stack.pop()
        
        ans = ""
        for c, times in stack:
            ans += c*times

        return ans