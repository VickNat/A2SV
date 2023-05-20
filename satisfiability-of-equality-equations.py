class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {i : i for i in range(97, 123)}
        size = {i : 1 for i in range(97, 123)}

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

            if size[x_rep] >= size[y_rep]:
                size[x_rep] += size[y_rep]
                parent[y_rep] = parent[x_rep]
            else:
                size[y_rep] += size[x_rep]
                parent[x_rep] = parent[y_rep]
        
        for elm in equations:
            x, y = ord(elm[0]), ord(elm[-1])

            if elm[1:3] == "==":
                union(x, y)

        for elm in equations:
            x, y = ord(elm[0]), ord(elm[-1])
            a = find(x)
            b = find(y)

            if a == b and elm[1] == "!":
                return False

        return True