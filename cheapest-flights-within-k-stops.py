class Solution:
    def dijkstra(self, graph, start, end, k):
        distances = {node: float('inf') for node, val in enumerate(graph)}
        distances[start] = 0

        priorityQueue = [(0, 0, start)]

        while priorityQueue:
            stops, curWeight, curNode = heappop(priorityQueue)

            if stops > k:
                continue

            for neighbour, weight in graph[curNode]:
                distance = curWeight+weight
                if distance < distances[neighbour] and stops <= k:
                    distances[neighbour] = distance
                    heappush(priorityQueue, (stops+1, distance, neighbour))

        return distances[end]


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for i in range(n)]

        for fro, to, weight in flights:
            graph[fro].append((to, weight))
        
        cheapest = self.dijkstra(graph, src, dst, k)

        return -1 if cheapest == float('inf') else cheapest