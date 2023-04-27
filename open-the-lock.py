class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([["0000", 0]])
        visited = set()
        visited.add("0000")
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        while queue:
            lock, path = queue.popleft()

            if lock == target:
                return path
            
            for i in range(4):
                temp = list(lock)
                val = 1 + int(temp[i])

                if val > 9:
                    val = 0
                temp[i] = str(val)

                if "".join(temp) not in deadends and "".join(temp) not in visited:
                    visited.add("".join(temp))
                    queue.append(["".join(temp), path+1])
                
                temp = list(lock)
                val = int(temp[i]) - 1
                if val < 0:
                    val = 9
                
                temp[i] = str(val)

                if "".join(temp) not in deadends and "".join(temp) not in visited:
                    visited.add("".join(temp))
                    queue.append(["".join(temp), path+1])
            
        return -1