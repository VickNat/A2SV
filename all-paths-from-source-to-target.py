class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)-1
        ans = []

        def dfs(idx, path):
            if idx == N:
                ans.append(path + [idx])
                return
            
            for i in range(len(graph[idx])):
                dfs(graph[idx][i], path + [idx])
        
        path = [0]
        for idx in range(len(graph[0])):
            dfs(graph[0][idx], path)
        
        return ans