class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        N = len(parent)
        graph = [[] for i in range(N)]
        maxPath = 0

        for i in range(N):
            if parent[i] == -1:
                continue
            
            graph[parent[i]].append(i)
        
        print(graph)
        
        def dfs(idx):
            nonlocal maxPath
            first = 0
            second = 0

            for elm in graph[idx]:
                child = dfs(elm)
                if s[elm] == s[idx]: continue

                if child > first:
                    second = first
                    first = child
                elif child > second:
                    second = child
            
            maxPath = max(maxPath, second+1+first)
            
            return first+1

        dfs(0)
        return maxPath