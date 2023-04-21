class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(idx):
            
            for i, elm in enumerate(isConnected[idx]):
                if i not in visited and elm == 1:
                    visited.add(i)
                    dfs(i)

        for idx in range(N):
            if idx not in visited:
                dfs(idx)
                provinces += 1

        return provinces