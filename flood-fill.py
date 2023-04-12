class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R = len(image)
        C = len(image[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[0 for i in range(C)] for j in range(R)]

        def inbound(r, c):
            return 0 <= r < R and 0 <= c < C and visited[r][c] == 0

        def dfs(r, c):
            visited[r][c] = 1
            temp = image[r][c]
            image[r][c] = color

            for row, col in directions:
                newR = r + row
                newC = c + col

                if inbound(newR, newC) and image[newR][newC] == temp:
                    dfs(newR, newC)
        
        dfs(sr, sc)
        return image