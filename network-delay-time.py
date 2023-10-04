class Solution:
    def dijkstra(self, graph, start):
        distances = {node: float('inf') for node, val in graph.items()}
        distances[start] = 0
        visited = set()

        priorityQueue = [(0, start)]

        while priorityQueue:
            curWeight, curNode = heappop(priorityQueue)

            if curNode in visited:
                continue
            
            visited.add(curNode)

            for neighbour, weight in graph[curNode]:
                distance = curWeight+weight
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heappush(priorityQueue, (distance, neighbour))

        return max(distances.values())

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {node: [] for node in range(1, n+1)}

        for ui, vi, w in times:
            graph[ui].append((vi, w))

        ans = self.dijkstra(graph, k)
        return  ans if ans != float('inf') else -1