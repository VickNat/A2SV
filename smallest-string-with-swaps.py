class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        parent = {i : i for i in range(N)}
        size = {i : 1 for i in range(N)}
        swaps = defaultdict(lambda: defaultdict(int))
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
                if size[x_rep] < size[y_rep]:
                    x_rep, y_rep = y_rep, x_rep
                
                parent[y_rep] = parent[x_rep]
                size[x_rep] += size[y_rep]
            
        # Unify the index pairs as nodes
        for a, b in pairs:
            union(a, b)
        
        # Keep the record of each parent's children
        for idx in range(N):
            par = find(idx)
            swaps[par][s[idx]] += 1
        
        # Add the minimum of each parent's value to answer
        for idx in range(N):
            par = find(idx)
            cur = min(swaps[par])
            swaps[par][cur] -= 1

            if not swaps[par][cur]:
                swaps[par].pop(cur)
            
            ans += cur
        
        return ans