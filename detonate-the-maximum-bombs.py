class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        graph = [[] for i in range(N)]
        detonated = 0
        visited = set()

        for first in range(N):
            for second in range(N):
                distance = math.sqrt(((bombs[second][0] - bombs[first][0])**2) + ((bombs[second][1] - bombs[first][1])**2))

                if bombs[first][2] >= distance and first != second:
                    graph[first].append(second)
        
        def dfs(idx):

            visited.add(idx)

            for elm in graph[idx]:
                if elm not in visited:
                    dfs(elm)
        
        for i in range(N):
            visited.clear()
            dfs(i)
            detonated = max(detonated, len(visited))

        return detonated