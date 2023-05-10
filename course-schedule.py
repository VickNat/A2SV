class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        indegree = [0 for i in range(numCourses)]
        outdegree = [[] for i in range(numCourses)]
        ans = []

        for a, b in prerequisites:
            indegree[a] += 1
            outdegree[b].append(a)

        for idx in range(numCourses):
            if indegree[idx] == 0:
                queue.append(idx)
        
        while queue:
            cur = queue.popleft()
            ans.append(cur)

            for elm in outdegree[cur]:
                indegree[elm] -= 1

                if indegree[elm] == 0:
                    queue.append(elm)
        
        if len(ans) != numCourses:
            return False
        
        return True