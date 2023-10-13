class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for i in range(n)]
        counts = 0

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(cur, prev):
            nonlocal counts
            sum_ = values[cur]

            for child in graph[cur]:
                if child != prev:
                    sum_ += dfs(child, cur)
            
            if sum_%k == 0:
                counts += 1
                return 0

            return sum_
        
        dfs(0, -1)
        return counts