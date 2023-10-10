class Solution:
    def dijkstra(self, graph, start, end):
        distances = {node: float('inf') for node, val in graph.items()}
        distances[start] = 1
        visited = set()

        priorityQueue = [(1, start)]

        while priorityQueue:
            curWeight, curNode = heappop(priorityQueue)

            if curNode in visited:
                continue
            
            visited.add(curNode)

            for neighbour, weight in graph[curNode]:
                distance = curWeight*weight
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heappush(priorityQueue, (distance, neighbour))

        return distances[end] if distances[end] != float('inf') else -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        N = len(values)
        M = len(queries)
        graph = defaultdict(list)
        
        for idx, val in enumerate(equations):
            first, sec = val
            graph[first].append((sec, float(values[idx])))
            graph[sec].append((first, 1/float(values[idx])))

        ans = []

        for first, second in queries:
            if first not in graph or second not in graph:
                ans.append(-1.00000)
            else:
                ans.append(float(self.dijkstra(graph, first, second)))

        return ans