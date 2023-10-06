class Solution:
    def knightDialer(self, n: int) -> int:
        rows = 4
        cols = 3
        numPad = [[-1 for c in range(cols)] for r in range(rows)]
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        num = 1
        for r in range(rows):
            flag = False
            for c in range(cols):
                numPad[r][c] = num
                num += 1
                if num > 9:
                    flag = True
                    break
            if flag:
                break
        numPad[3][1] = 0

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        MOD = ((10**9)+7)
        @cache
        def dp(r, c, phone):
            if phone == n:
                return 1
            if phone > n:
                return 0
            
            dials = 0
            for changeR, changeC in directions:
                newR = r+changeR
                newC = c+changeC

                if inbound(newR, newC) and numPad[newR][newC] != -1:
                    dials += dp(newR, newC, phone+1)

            return dials%((10**9)+7)

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if numPad[r][c] != -1:
                    ans += dp(r, c, 1)
        
        return ans%((10**9)+7)