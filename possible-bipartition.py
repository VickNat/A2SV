class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        bipartite = [0]*n
        adjList = [[] for i in range(n)]
        visited = set()

        for node1, node2 in dislikes:
            adjList[node1-1].append(node2-1)
            adjList[node2-1].append(node1-1)

        def dfs(person):

            visited.add(person)

            for p in adjList[person]:
                if bipartite[p] == bipartite[person]:
                    return False

                if bipartite[p] == 0:
                    bipartite[p] += 3-bipartite[person]

            for p in adjList[person]:
                if p not in visited and not dfs(p):
                    return False
            
            return True

        for idx in range(n):
            if idx not in visited:
                bipartite[idx] = 1

                if not dfs(idx):
                    return False
        return True