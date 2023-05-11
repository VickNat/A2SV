class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        ans = [i for i in range(N)]
        indegree = [0 for i in range(N)]
        outdegree = [[] for i in range(N)]
        queue = deque()

        for a, b in richer:
            indegree[b] += 1
            outdegree[a].append(b)

        for idx, counts in enumerate(indegree):
            if counts == 0:
                queue.append(idx)

        while queue:
            cur= queue.popleft()

            for elm in outdegree[cur]:
                indegree[elm] -= 1

                if quiet[ans[cur]] < quiet[ans[elm]]:
                    ans[elm] = ans[cur]
                
                if indegree[elm] == 0:
                    queue.append(elm)
        
        return ans