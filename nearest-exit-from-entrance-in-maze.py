class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        queue = deque([(entrance[0], entrance[1])])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        levels = 0

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        while queue:
            N = len(queue)

            for _ in range(N):
                r, c = queue.popleft()

                for changeR, changeC in directions:
                    newR = r + changeR
                    newC = c + changeC

                    if (newR, newC) not in visited:
                        if not inbound(newR, newC) and [r, c] != entrance:
                            return levels

                        if inbound(newR, newC) and maze[newR][newC] != "+":
                            queue.append((newR, newC))
                            visited.add((newR, newC))
            
            levels += 1
    
        return -1