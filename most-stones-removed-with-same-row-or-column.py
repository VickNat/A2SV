class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {tuple(stone) : tuple(stone) for stone in stones}
        size = {tuple(stone) : 1 for stone in stones}
        
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
        
        for idx, first in enumerate(stones):
            for j in range(len(stones)):
                sec = stones[j]
                if first[0] == sec[0] or first[1] == sec[1]:
                    union(tuple(first), tuple(sec))
        
        ans = 0
        visited = set()

        for elm in stones:
            val = find(tuple(elm))
            if val not in visited:
                ans += size[val]-1
                visited.add(val)
        
        return ans