class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.minimum = float('inf')
        children = [0]*k
        cookies.sort(reverse=True)

        def backtrack(i, children):
            if i >= len(cookies):
                self.minimum = min(self.minimum, max(children))
                return 
            
            if max(children) >= self.minimum:
                return

            for j in range(k):
                children[j] += cookies[i]
                backtrack(i+1, children)
                children[j] -= cookies[i]
            
        backtrack(0, children)
        return self.minimum