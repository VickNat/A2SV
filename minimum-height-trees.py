class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        queue = deque()
        indegree = [0 for i in range(n)]
        degree = [[] for i in range(n)]
        ans = [0]

        for a, b in edges:
            degree[a].append(b)
            degree[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        for idx, elm in enumerate(indegree):
            if elm == 1:
                queue.append(idx)
        
        while queue:
            N = len(queue)
            temp = []

            for _ in range(N):
                cur = queue.popleft()
                temp.append(cur)

                for elm in degree[cur]:
                    indegree[elm] -= 1
                    
                    if indegree[elm] == 1:
                        queue.append(elm)
            
            ans = temp[:]

        return ans