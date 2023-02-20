class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        for r in range(rows):
            rowDict = defaultdict(int)
            
            for c in range(cols):
                if board[r][c] != ".":
                    rowDict[board[r][c]] += 1
                
                if rowDict[board[r][c]] > 1:
                    return False
        
        for c in range(cols):
            colDict = defaultdict(int)
            
            for r in range(rows):
                if board[r][c] != ".":
                    colDict[board[r][c]] += 1
                
                if colDict[board[r][c]] > 1:
                    return False
        
        sRow = 0
        
        while sRow + 3 <= rows:
            sCol = 0
            
            while sCol + 3 <= cols:
                checkDict = defaultdict(int)
                
                for r in range(sRow, sRow + 3):
                    for c in range(sCol, sCol + 3):
                        if board[r][c] != ".":
                            checkDict[board[r][c]] += 1
                        
                        if checkDict[board[r][c]] > 1:
                            return False
                
                sCol += 3
            
            sRow += 3
            
        return True
                
                
                
                