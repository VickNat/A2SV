class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = [[0 for i in range(cols)] for j in range(rows)]

        def inbound(r, c):
            return (0 <= r < rows) and (0 <= c < cols)

        def dfs(r, c):
            visited[r][c] = 1

            for changeR, changeC in directions:
                newR = r + changeR
                newC = c + changeC

                if inbound(newR, newC) and visited[newR][newC] == 0 and board[newR][newC] == "O":
                    dfs(newR, newC)
 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    continue

                for changeR, changeC in directions:
                    newR = r + changeR
                    newC = c + changeC

                    if not inbound(newR, newC) and visited[r][c] == 0:
                        dfs(r, c)
                
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and board[r][c] == "O":
                    board[r][c] = "X"