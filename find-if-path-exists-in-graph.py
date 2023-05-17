class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]

        def find(idx):
            root = parent[idx]

            while root != parent[root]:
                root = parent[root]
            
            while idx != root:
                temp = parent[idx]
                parent[idx] = root
                idx = temp
            
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
        
        for x, y in edges:
            union(x, y)
                
        return find(source) == find(destination)