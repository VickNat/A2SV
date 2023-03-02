class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        size = len(s)

        for elm in s:
            if not stack or elm == '(':
                stack.append(elm)
            elif stack and stack[-1] == '(' and elm == ')':
                stack.pop()
                stack.append(1)
            elif stack and stack[-1] != '(' and elm == ')':
                total = 0

                while stack and stack[-1] != '(':
                    total += stack[-1]
                    stack.pop()

                total *= 2
                stack.pop()
                stack.append(total)
        
        sums = 0
        while stack:
            sums += stack[-1]
            stack.pop()
        
        return sums