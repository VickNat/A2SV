class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        N = len(adjacentPairs) + 1
        nums = []
        visited = set()
        graph = defaultdict(list)
        queue = deque()

        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        
        for key, val in graph.items():
            if len(val) == 1:
                queue.append(key)
                visited.add(key)
                break

        while queue:
            cur = queue.popleft()
            nums.append(cur)

            for elm in graph[cur]:
                if elm not in visited:
                    visited.add(elm)
                    queue.append(elm)

        return nums