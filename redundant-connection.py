class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i+1 for i in range(n)]
        size = [1 for i in range(n)]
        ans = []

        def find(x):
            root = x

            while root != parent[root-1]:
                root = parent[root-1]
            
            while x != parent[x-1]:
                temp = parent[x-1]
                parent[x-1] = root
                x = temp
            
            return root
            
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)

            if x_rep != y_rep:
                if size[x_rep-1] >= size[y_rep-1]:
                    size[x_rep-1] += size[y_rep-1]
                    parent[y_rep-1] = parent[x_rep-1]
                else:
                    size[y_rep-1] += size[x_rep-1]
                    parent[x_rep-1] = parent[y_rep-1]
            else:
                ans.append([x, y])
        
        for x, y in edges:
            union(x, y)
        
        return ans[-1]