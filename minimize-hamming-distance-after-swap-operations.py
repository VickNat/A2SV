class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        N = len(source)
        parent = [i for i in range(N)]
        size = [1 for i in range(N)]
        swaps = defaultdict(lambda: defaultdict(int))

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

        for a, b in allowedSwaps:
            union(a, b)
        
        for idx in range(N):
            par = find(idx)
            swaps[par][source[idx]] += 1
        

        counts = 0
        for idx in range(N):
            par = find(idx)

            if target[idx] in swaps[par]:
                swaps[par][target[idx]] -= 1

                counts += 1
                if not swaps[par][target[idx]]:
                    swaps[par].pop(target[idx])
        
        return N-counts