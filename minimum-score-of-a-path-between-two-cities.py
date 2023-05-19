class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = {i : i for i in range(1, n+1)}
        size = {i : 1 for i in range(1, n+1)}
        ans = float('inf')

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
            nonlocal ans

            x_rep = find(x)
            y_rep = find(y)

            if size[x_rep] >= size[y_rep]:
                size[x_rep] += size[y_rep]
                parent[y_rep] = parent[x_rep]
            else:
                size[y_rep] += size[x_rep]
                parent[x_rep] = parent[y_rep]

        for a, b, d in roads:
            union(a, b)
        
        for a, b, d in roads:
            if find(1) == find(a):
                ans = min(ans, d)
        
        return ans