class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for i in range(n)]
        indegree = [0 for i in range(n)]
        outdegree = [[] for i in range(n)]
        queue = deque()

        for a, b in edges:
            indegree[b] += 1
            outdegree[a].append(b)
        
        for idx, counts in enumerate(indegree):
            if counts == 0:
                queue.append(idx)
        
        while queue:
            cur = queue.popleft()

            for elm in outdegree[cur]:
                indegree[elm] -= 1

                ans[elm] = ans[elm].union(ans[cur])
                ans[elm].add(cur)

                if indegree[elm] == 0:
                    queue.append(elm)
        
        for idx in range(n):
            ans[idx] = sorted(list(ans[idx]))

        return ans