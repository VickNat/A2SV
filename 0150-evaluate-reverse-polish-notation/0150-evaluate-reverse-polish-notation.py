class Solution:
    def isOperator(self, operator) -> bool:
        operators = defaultdict(int)
        operators['+'] = 0
        operators['-'] = 0
        operators['*'] = 0
        operators['/'] = 0
        
        return operator in operators
    
    def operation(self, a, b, elm) -> int:
        res = 0
        
        if elm == '+':
            res = int(b+a)
        elif elm == '-':
            res = int(b-a)
        elif elm == '*':
            res = int(b*a)
        elif elm == '/':
            res = int(b/a)
        
        return res
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for elm in tokens:
            if self.isOperator(elm):
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                
                res = self.operation(a, b, elm)
                stack.append(res)
            else:
                stack.append(int(elm))
            
        return stack[-1]
        