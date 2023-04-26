class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for i in range(n)]
        visited = set()
        subtrees = [0]*n
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(node):

            visited.add(node)
            result = defaultdict(int)
            result[labels[node]] += 1
            
            for elm in graph[node]:
                if elm not in visited:
                    child = dfs(elm)
                    for l in child:
                        result[l] += child[l]
            
            subtrees[node] += result[labels[node]]
            return result

        dfs(0)
        return subtrees