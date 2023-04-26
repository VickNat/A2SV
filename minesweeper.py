class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            if board[r][c] == "M":
                board[r][c] = "X"
                return
            
            adjMines = 0

            for changeR, changeC in directions:
                newR = r + changeR
                newC = c + changeC

                if inbound(newR, newC) and board[newR][newC] == "M":
                    adjMines += 1

            if adjMines > 0:
                board[r][c] = str(adjMines)
                return
            
            board[r][c] = "B"

            for changeR, changeC in directions:
                newR = r + changeR
                newC = c + changeC

                if inbound(newR, newC) and board[newR][newC] == "E":
                    dfs(newR, newC)

        dfs(click[0], click[1])
        return board