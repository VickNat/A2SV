class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        ans = [[0 for c in range(cols)] for r in range(rows)]
        visited = set()
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append([r, c, 0])
                    visited.add((r, c))
        
        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        while queue:
            r, c, path = queue.popleft()

            for changeR, changeC in directions:
                newR = r + changeR
                newC = c + changeC

                if inbound(newR, newC) and (newR, newC) not in visited:
                    ans[newR][newC] = path+1
                    queue.append([newR, newC, path+1])
                    visited.add((newR, newC))

        return ans