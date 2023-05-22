class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        if N == 0:
            return 0
        parent = [i for i in range(N)]
        size = [1 for i in range(N)]
        edges = []
        distance = 0

        for idx1 in range(N):
            xi, yi = points[idx1]
            for idx2 in range(idx1+1, N):
                if idx1 != idx2:
                    x = abs(xi-points[idx2][0])
                    y = abs(yi-points[idx2][1])
                    dist = x+y

                    edges.append((dist, idx1, idx2))

        def find(x):
            root = x

            while root != parent[root]:
                root = parent[root]
            
            while x != parent[x]:
                temp = parent[x]
                parent[x] = root
                x = temp
            
            return root

        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)

            if x_rep != y_rep:
                if size[x_rep] >= size[y_rep]:
                    size[x_rep] += size[y_rep]
                    parent[y_rep] = parent[x_rep]
                else:
                    size[y_rep] += size[x_rep]
                    parent[x_rep] = parent[y_rep]
        
        edges.sort()

        for dist, start, end in edges:
            if find(start) != find(end):
                distance += dist

            union(start, end)
        
        return distance