class Solution:
    def racecar(self, target: int) -> int:
        visited = set()
        visited.add((0, 1))
        queue = deque([(0, 1, 0)])
        path = 0

        while queue:
            position, speed, path = queue.popleft()
            
            if position == target:
                return path

            if (position+speed, 2*speed) not in visited:
                queue.append((position+speed, 2*speed, path+1))
                visited.add((position+speed, 2*speed))
            
            if speed > 0:
                if (position, -1) not in visited:
                    queue.append((position, -1, path+1))
                    visited.add((position, -1))
            else:
                if (position, 1) not in visited:
                    queue.append((position, 1, path+1))
                    visited.add((position, 1))