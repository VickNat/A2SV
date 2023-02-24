class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for elm in logs:
            if elm == "../":
                if len(stack) > 0:
                    stack.pop()
            
            elif elm == "./":
                continue
            else:
                stack.append(elm)
            
        return len(stack)