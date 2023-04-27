class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()
        visited.add(0)

        while queue:
            key = queue.popleft()

            for elm in rooms[key]:
                if elm not in visited:
                    visited.add(elm)
                    queue.append(elm)
        
        return len(visited) == len(rooms)