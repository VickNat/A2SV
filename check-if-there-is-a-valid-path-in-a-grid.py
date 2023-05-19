class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        directions = {1: ("l", "r"), 2: ("u", "d"), 3: ("l", "d"), 4: ("r", "d"), 5: ("u", "l"), 6: ("u", "r")}
        newDir = {"r": (0, 1), "d": (1, 0)}
        parent = {}
        size = {}

        for r in range(rows):
            for c in range(cols):
                parent[(r, c)] = (r, c)
                size[(r, c)] = 1
        
        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        # TODO: union and find
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

        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                for dir in directions[cell]:
                    if dir == "r" or dir == "d":
                        changeR, changeC = newDir[dir]
                        newR = r + changeR
                        newC = c + changeC

                        if inbound(newR, newC):
                            if dir == "r" and "l" in directions[grid[newR][newC]]:
                                union((r, c), (newR, newC))
                            
                            elif dir == "d" and "u" in directions[grid[newR][newC]]:
                                union((r, c), (newR, newC))
                            
        return find((0, 0)) == find((rows-1, cols-1))