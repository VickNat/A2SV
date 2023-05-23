class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        ans = []

        def find(x):
            root = x

            while root != parent[root]:
                root = parent[root]
            
            while x != parent[x]:
                x, parent[x] = parent[x], root

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
        
        for a, b in requests:
            friends = True
            parA = find(a)
            parB = find(b)

            for ra, rb in restrictions:
                ra = find(ra)
                rb = find(rb)

                if (parA == ra and parB == rb) or (parA == rb and parB == ra):
                    friends = False
                    break
            
            if friends:
                union(parA, parB)
            
            ans.append(friends)
        
        return ans