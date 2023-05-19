class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {i : i for i in range(97, 123)}
        ans = ""

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
                if parent[x_rep] <= parent[y_rep]:
                    parent[y_rep] = parent[x_rep]
                else:
                    parent[x_rep] = parent[y_rep]
        
        for i in range(len(s1)):
            union(ord(s1[i]), ord(s2[i]))

        for i in range(len(baseStr)):
            ans += chr(find(ord(baseStr[i])))
        
        return ans