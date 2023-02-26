class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = defaultdict(int)
        operators['+'] = 0
        operators['-'] = 0
        operators['*'] = 0
        operators['/'] = 0
        
        for elm in tokens:
            if elm in operators:
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                res = 0
                
                if elm == '+':
                    res = int(b+a)
                elif elm == '-':
                    res = int(b-a)
                elif elm == '*':
                    res = int(b*a)
                elif elm == '/':
                    res = int(b/a)
                
                stack.append(res)
            else:
                stack.append(int(elm))
            
        return stack[-1]
        