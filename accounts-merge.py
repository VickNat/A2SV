class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        size = {}
        ans = []

        for elm in accounts:
            for i in range(1, len(elm)):
                parent[elm[i]] = elm[i]
                size[elm[i]] = set([elm[i]])
                
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
                if len(size[x_rep]) >= len(size[y_rep]):
                    size[x_rep] |= size[y_rep]
                    parent[y_rep] = parent[x_rep]
                    size[y_rep].clear()
                else:
                    size[y_rep] |= size[x_rep]
                    parent[x_rep] = parent[y_rep]
                    size[x_rep].clear()
        
        for elm in accounts:
            for i in range(1, len(elm)):
                for j in range(i+1, len(elm)):
                    union(elm[i], elm[j])
        
        visited = set()
        for elm in accounts:
            name = elm[0]
            temp = find(elm[1])

            if size[temp] and temp not in visited:
                val = list(set(size[temp]))
                ans.append([name] + sorted(val))
                visited.add(temp)

        return ans