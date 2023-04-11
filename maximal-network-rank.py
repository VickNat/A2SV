class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        ans = 0

        for idx1, idx2 in roads:
            graph[idx1].add(idx2)
            graph[idx2].add(idx1)
        
        for i in range(n-1):
            for j in range(i+1, n):
                size = len(graph[i])+len(graph[j])

                if i in graph[j]:
                    size -= 1
                
                ans = max(ans, size)
        
        return ans