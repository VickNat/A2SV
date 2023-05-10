class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0 for i in range(len(graph))]
        ans = []

        def dfs(node):
            if colors[node] == 2:
                return True
            if colors[node] == 1:
                return False
            
            colors[node] = 1

            for child in graph[node]:
                call = dfs(child)
                if not call:
                    return False
            
            colors[node] = 2
            return True

        for idx in range(len(graph)):
            if dfs(idx):
                ans.append(idx)
        
        return ans