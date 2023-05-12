class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        colors = [[0, 0] for i in range(N)]
        indegree = [0 for i in range(N)]
        maxCycle = -1

        for idx, elm in enumerate(edges):
            if elm != -1:
                indegree[elm] += 1
        
        def dfs(idx, curPath):
            nonlocal maxCycle
            if idx == -1:
                return
            if colors[idx][0] == 1:
                return
            if colors[idx][0] == 2:
                maxCycle = max(maxCycle, (curPath-colors[idx][1])+1)
                return
            
            colors[idx][0] = 2
            colors[idx][1] += curPath+1

            dfs(edges[idx], curPath+1)

            colors[idx][0] = 1
        
        for idx, count in enumerate(indegree):
            dfs(idx, 0)
        
        return maxCycle