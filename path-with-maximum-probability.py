class Solution:
    def dijkstra(self, graph, start, end):
        distances = {node: 0 for node, val in enumerate(graph)}
        distances[start] = 0
        visited = set()

        priorityQueue = [(-1, start)]

        while priorityQueue:
            curWeight, curNode = heappop(priorityQueue)
            curWeight = abs(curWeight)

            if curNode in visited:
                continue
            
            visited.add(curNode)

            for neighbour, weight in graph[curNode]:
                distance = curWeight*weight
                if distance > distances[neighbour]:
                    distances[neighbour] = distance
                    heappush(priorityQueue, (-distance, neighbour))

        return distances[end]

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for i in range(n)]

        for idx, val in enumerate(edges):
            u, v = val
            graph[u].append((v, succProb[idx]))
            graph[v].append((u, succProb[idx]))
        
        ans = self.dijkstra(graph, start_node, end_node)
        return ans