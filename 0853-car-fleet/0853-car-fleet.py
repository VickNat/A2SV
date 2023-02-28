class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        length = len(position)
        time = []
        
        for idx in range(length):
            distance = target - position[idx]
            time.append([distance, distance/speed[idx]])
            
        time.sort()

        for dist, elm in time:
            if not stack or stack[-1] < elm:
                stack.append(elm)
                        
        return len(stack)