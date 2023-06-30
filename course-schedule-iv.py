class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queue = deque()
        ancestors = [[False for j in range(numCourses)] for i in range(numCourses)]
        outdegree = [[] for i in range(numCourses)]
        ans = []

        for a, b in prerequisites:
            outdegree[b].append(a)
        
        for i in range(numCourses):
            queue.append(i)
            visited = set()

            while queue:
                cur = queue.popleft()
                visited.add(cur)

                for elm in outdegree[cur]:
                    ancestors[i][elm] = True

                    if elm not in visited:
                        queue.append(elm)
        
        for u, v in queries:
            ans.append(ancestors[v][u])

        return ans